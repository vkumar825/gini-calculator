import numpy as np
from matplotlib import pyplot as plt


def gini():
    print("Welcome to Simple Gini coefficient Calculator!")
    print("To get started, enter the number of incomes to get")
    print("the Gini coefficient, and the graph of Lorenz curve.\n")
    while True:
        try:
            individual_amount = int(input("Number Of Individual(s): "))
            individual_counter = 0
            individual_income = []

            while individual_counter < individual_amount:
                individual_income_input = int(input("Income: $"))
                if individual_income_input >= 0:
                    individual_counter += 1
                    individual_income.append(individual_income_input)
                else:
                    print("Income cannot be less than 0.")

            # Calculating the percentage of the population
            percentage_pop = []
            for i in range(len(individual_income) + 1):
                percent_p = (i / len(individual_income))
                percentage_pop.append(percent_p)
            percentage_pop = np.array(percentage_pop)

            # Calculating the percentage of the income
            percentage_income = []
            percentage_income.insert(0, 0)
            for i in range(len(individual_income)):
                percent_i = (individual_income[i] / sum(individual_income))
                percentage_income.append(percent_i)
            percentage_income = np.array(percentage_income)

            # Calculating the cumulative income
            cum_income = np.cumsum(percentage_income)

            # Calculating the Gini coefficient
            temp = []
            area_under_curve = []
            individual_income.insert(0, 0)
            for i in range(len(cum_income) - 1):
                sum_val = cum_income[i] + cum_income[i + 1]
                temp.append(sum_val)
            for j in range(len(temp)):
                curve_val = (temp[j] / 2) * (1 / (len(individual_income) - 1))
                area_under_curve.append(curve_val)
            gini_coefficient = (0.5 - sum(area_under_curve)) / 0.5
            print("\nGini coefficient: {:.2f}".format(gini_coefficient))

            # Displaying the graph of Lorenz Curve
            print("Display Lorenz Curve? (Y/N)")
            choice = str(input(""))

            if choice.capitalize() == "Y":
                plt.plot(percentage_pop, percentage_pop, label="Line Of Equality")
                plt.plot(percentage_pop, cum_income, label="Lorenz Curve")
                plt.legend(loc="upper left")
                plt.show()
                break
            else:
                break

        except ValueError:
            print("Not a valid value, please try again.\n")


if __name__ == '__main__':
    gini()


