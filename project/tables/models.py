from django.db import models

# Create your models here.
class Neighborhood(models.Model):
    # id = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    name = models.CharField(max_length=100)
    # borough = models.CharField()

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "name": self.name,
            # "borough": self.borough,
        }

class Ages(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    # borough = models.ForeignKey(Borough)
    age_0_19 = models.DecimalField(max_digits=10, decimal_places=5)
    age_20_24 = models.DecimalField(max_digits=10, decimal_places=5)
    age_25_34 = models.DecimalField(max_digits=10, decimal_places=5)
    age_35_64 = models.DecimalField(max_digits=10, decimal_places=5)
    age_65_over = models.DecimalField(max_digits=10, decimal_places=5)
    age_median = models.DecimalField(max_digits=10, decimal_places=5)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood,
            # "borough": self.borough,
            "age_0_19": self.age_0_19,
            "age_20_24": self.age_20_24,
            "age_25_34": self.age_25_34,
            "age_35_64": self.age_35_64,
            "age_65_over": self.age_65_over,
            "age_median": self.age_median, 
        }

class Economic(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    # borough = models.ForeignKey(Borough)
    laborforce = models.DecimalField(max_digits=10, decimal_places=5)
    unemployed = models.DecimalField(max_digits=10, decimal_places=5)
    below_poverty_level = models.DecimalField(max_digits=10, decimal_places=5)
    income_0_50 = models.DecimalField(max_digits=10, decimal_places=5)
    income_50_100 = models.DecimalField(max_digits=10, decimal_places=5)
    income_100_200 = models.DecimalField(max_digits=10, decimal_places=5)
    income_200_plus = models.DecimalField(max_digits=10, decimal_places=5)
    median_income = models.DecimalField(max_digits=10, decimal_places=5)
    mean_income = models.DecimalField(max_digits=10, decimal_places=5)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood.name,
            # "borough": self.borough,
            "laborforce": self.laborforce,
            "unemployed": self.unemployed,
            "below_poverty_level": self.below_poverty_level,
            "income_0_50": self.income_0_50,
            "income_50_100": self.income_50_100, 
            "income_100_200": self.income_100_200,
            "income_200_plus": self.income_200_plus,
            "median_income": self.median_income,
            "mean_income": self.mean_income,
        }

# all other tables point here with FKs