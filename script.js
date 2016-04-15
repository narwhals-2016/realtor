// we get all the neighborhoods by selecting the parent id of map and then getting all the children
var neighborhood = $("svg.V_DCP_NEIGHBORHOOD").children;
// define new click events
var event = new Event('click');
​
// getting to the right place
var scrapeData = function(widgetId, toggleWidgetId, current_index){
    // reseting the NH to the current one in the list created above
    profileState.selectedIds = [neighborhood[current_index].id.split('.')[1]]; 
    // building the click event to act on each tab
    $('[widgetid="' + toggleWidgetId + '"]').dispatchEvent(event);
    
    // go back to a different tab to then go download a new excel - ?!
    var toggle = function(widgetId, toggleWidgetId, current_index){
        return function(){
        $('[widgetid="' + widgetId + '"]').dispatchEvent(event);
            console.log(profileState);
            profileState.jsonData = ""
            setTimeout(acsExcel(widgetId, toggleWidgetId, current_index), 3000);
        }
    };
    setTimeout(toggle(widgetId1, toggleWidgetId, current_index),3000);
};
​
// downloading the file
function acsExcel(widgetId, toggleWidgetId, current_index) {
    return function(){
        // this check if the one above it has been completed, if not we timeout again 
        if (profileState.jsonData === ""){
            console.log('TimeOut');
            setTimeout(acsExcel(widgetId, toggleWidgetId, current_index), 3000);
            return false;
        }
        console.log('Tag');
        // if not then we dowload it 
        dojo.byId("acsExcelForm").acsExcelContent.value = JSON.stringify(profileState.jsonData);
        dojo.byId("acsExcelForm").submit();
        scrapeData(widgetId, toggleWidgetId, --current_index);
        return true
    };
};
​
// this is where we redefine things based on getting the values from the page
var currentWidgetId = 'acsContainer_tablist_dcp_pa_AcsDemo_0';
var toggleWidgetId = 'acsContainer_tablist_dcp_pa_AcsSocial_0';
scrapeData(currentWidgetId, toggleWidgetId, --neighborhood.length);


