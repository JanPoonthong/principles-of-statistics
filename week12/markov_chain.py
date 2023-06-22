import numpy as np

states = ["Temple", "Floating", "Night"]

transitionName = [["TT", "TF", "TN"], ["FT", "FF", "FN"], ["NT", "NF", "NN"]]

transitionMatrix = [[0.6, 0.2, 0.2], [0.4, 0.5, 0.1], [0.2, 0.1, 0.7]]

if (
    sum(transitionMatrix[0])
    + sum(transitionMatrix[1])
    + sum(transitionMatrix[2])
    != 3
):
    print("Somewhere, something went wrong. Transition matrix, perhap?")
else:
    print("All is gonnabe okay, you should move on !!")


def activity_forecast(days):
    activity_today = "Temple"
    print("Start state: " + activity_today)
    activityList = [activity_today]
    i = 1
    prob = 1
    while i != days:
        if activity_today == "Temple":
            change = np.random.choice(
                transitionName[0], replace=True, p=transitionMatrix[0]
            )
        if change == "TT":
            prob = prob * 0.6
            activityList.append("Temple")
            pass
        elif change == "TF":
            prob = prob * 0.2
            activity_today = "FLoating"
            activityList.append("FLoating")
        else:
            prob = prob * 0.2
            activity_today = "Night"
            activityList.append("Night")

        if activity_today == "FLoating":
            change = np.random.choice(
                transitionName[1], replace=True, p=transitionMatrix[1]
            )
        if change == "FF":
            prob = prob * 0.5
            activityList.append("FLoating")
            pass
        elif change == "FT":
            prob = prob * 0.4
            activity_today = "Temple"
            activityList.append("Temple")
        else:
            prob = prob * 0.1
            activity_today = "Night"
            activityList.append("Night")

        if activity_today == "Night":
            change = np.random.choice(
                transitionName[2], replace=True, p=transitionMatrix[2]
            )
        if change == "NN":
            prob = prob * 0.7
            activityList.append("Night")
            pass
        elif change == "NT":
            prob = prob * 0.2
            activity_today = "Temple"
            activityList.append("Temple")
        else:
            prob = prob * 0.1
            activity_today = "FLoating"
            activityList.append("Floating")

        i += 1
        print("Possible state: " + str(activityList))
        print("End state after: " + str(days) + "days" + activity_today)
        print("Probability of the possible sequence of states: " + str(prob))


activity_forecast(2)
