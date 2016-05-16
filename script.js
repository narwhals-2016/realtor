/*
Script to automatically download neighborhood census excel files from maps.nyc.gov/census/ for all NYC neighborhoods
Type of file to download is set in the variable currentWidgetId. Types: Housing, Demographic, Economic, Social
Run script in devtools console to download files.
*/



// Collect All the Neighborhoods from the Map SVG
var neighborhood = $("svg.V_DCP_NEIGHBORHOOD").children;

// Create Fake Click Event
var event = new Event('click');

// This is the tab we want to collect Information From
var currentWidgetId = 'acsContainer_tablist_dcp_pa_AcsHousing_0';

// This is the tab we will switch to so we can clear the cached data.
// If the browser is on the tab we want it will not request new data 
// even if we change the current Neighborhood. 
var toggleWidgetId = 'acsContainer_tablist_dcp_pa_AcsEconomic_0';



var scrapeData = function(widgetId, toggleWidgetId, current_index, $){
    if (current_index === -1){
        return false;
    }
    // Here we set the id of the neighborhood we want to get information about
    profileState.selectedIds = [neighborhood[current_index].id.split('.')[1]]; 
    
    // This Step Clears The cached/previous Information.
    // After this we can switch to the tab we want information from. 
    $('[widgetid="' + toggleWidgetId + '"]').dispatchEvent(event);
    
    // This Function builds a Function for setTimeout to use
    // AKA: It builds the callback for setTimeout
    var toggle = function(widgetId, toggleWidgetId, current_index, $){
        // This Step is important. It creates a scope containing the current values of 
        // each of our variables. 
        // **setTimeout executes its callback in the global scope**
        // Creating a function here creates a scope that will remain when setTimeout executes the callback.
        return function(){
            // Clear old data if any exists.
            // This will also help us determine when the new data has come in.
            profileState.jsonData = ""

            // Here we fake a click event on the Tab we want data from.
            // This will send a request to the server asyncronously
            $('[widgetid="' + widgetId + '"]').dispatchEvent(event);

            // acsExcel will start the process of requesting an excel download.
            // We use setTimeout here because we want to wait 
            // until the asyncronous request, caused by line 42, gets a response with data.
            setTimeout(acsExcel(widgetId, toggleWidgetId, current_index, $), 3000);
        };
    };

    // Using setTimeout here allows us to space out our requests.
    // It also clears the stack and allows the function we are in to finish running.
    setTimeout(toggle(widgetId, toggleWidgetId, current_index, $), 3000);
    return false;
};

// This function creates a function object that will be called by setTimeout.(#47,#68)
function acsExcel(widgetId, toggleWidgetId, current_index, $) {
    // We return a function to ensure the values of `widgetId`, `toggleWidgetId` and `current_index` 
    // are what we expect. It `Locks` those values in the scope that travels with this 
    // function object into the setTimeouts.
    return function(){
        // We check `profileState.jsonData` here because if it is an empty string then we know 
        // the server has not responded to our request for data. 
        if (profileState.jsonData === ""){
            // If the server has not responded we do not want to try to download the excel.
            // So we call setTimeout in hopes that the server will respond in 3 seconds
            setTimeout(acsExcel(widgetId, toggleWidgetId, current_index, $), 3000);
            // We return here to stop the function from doing anything else. 
            return false;
        }
        // This is code I copied directly from the websites acsExcel function. It does exactly what the 
        // excel button does on the top right of data view.
        dojo.byId("acsExcelForm").acsExcelContent.value = JSON.stringify(profileState.jsonData);
        dojo.byId("acsExcelForm").submit();
        // Here we call srapeData again on the next index
        setTimeout(scrapeData(widgetId, toggleWidgetId, --current_index, $),0);
        return true;
    };
};


scrapeData(currentWidgetId, toggleWidgetId, --neighborhood.length, $); 