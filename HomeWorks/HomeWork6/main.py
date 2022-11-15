import math
from enum import Enum
import random
from sklearn import datasets
import matplotlib.pyplot as plt


class IrisClass(Enum):
    IrisSetosa = 0
    IrisVersicolour = 1
    IrisVerginica = 2


class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, iris_class):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.iris_class = iris_class


def load_data():
    iris = datasets.load_iris()
    prepared_data = []

    for i in range(len(iris.data)):
        prepared_data.append(Iris(iris.data[i][0], iris.data[i][1], iris.data[i][2], iris.data[i][3], iris.target[i]))

    return prepared_data


def reshafle_data(data):
    reshafled_data = []

    while len(data) > 0:
        index = random.randint(0, len(data) - 1)
        reshafled_data.append(data.pop(index))

    return reshafled_data


def normalize_data(data):
    min = [math.inf, math.inf, math.inf, math.inf]
    max = [-1, -1, -1, -1]
    normalized_data = []
    for item in data:
        if item.sepal_length > max[0]:
            max[0] = item.sepal_length
        if item.sepal_length < min[0]:
            min[0] = item.sepal_length

        if item.sepal_width > max[1]:
            max[1] = item.sepal_width
        if item.sepal_width < min[1]:
            min[1] = item.sepal_width

        if item.petal_length > max[2]:
            max[2] = item.petal_length
        if item.petal_length < min[2]:
            min[2] = item.petal_length

        if item.petal_width > max[3]:
            max[3] = item.petal_width
        if item.petal_width < min[3]:
            min[3] = item.petal_width

    for item in data:
        normalized_data.append(
            Iris(
                (item.sepal_length - min[0]) / (max[0] - min[0]),
                (item.sepal_width - min[1]) / (max[1] - min[1]),
                (item.petal_length - min[2]) / (max[2] - min[2]),
                (item.petal_width - min[3]) / (max[3] - min[3]),
                item.iris_class))

    return (min, max, normalized_data)


def get_color(iris_class):
    if iris_class == IrisClass.IrisSetosa.value:
        return "green"
    elif iris_class == IrisClass.IrisVerginica.value:
        return "yellow"
    else:
        return "red"


def print_projections(data, norm_data):
    fig, axes = plt.subplots(4, 4)

    axes[0, 1].scatter(x=[iris.sepal_length for iris in data], y=[iris.sepal_width for iris in data],
                       c=[get_color(iris.iris_class) for iris in data])
    axes[0, 1].set_xlabel('sepal_length')
    axes[0, 1].set_ylabel('sepal_width')

    axes[0, 2].scatter(x=[iris.sepal_length for iris in data], y=[iris.petal_length for iris in data],
                       c=[get_color(iris.iris_class) for iris in data])
    axes[0, 2].set_xlabel('sepal_length')
    axes[0, 2].set_ylabel('petal_length')

    axes[0, 3].scatter(x=[iris.sepal_length for iris in data], y=[iris.petal_width for iris in data],
                       c=[get_color(iris.iris_class) for iris in data])
    axes[0, 3].set_xlabel('sepal_length')
    axes[0, 3].set_ylabel('petal_width')

    axes[1, 2].scatter(x=[iris.sepal_width for iris in data], y=[iris.petal_length for iris in data],
                       c=[get_color(iris.iris_class) for iris in data])
    axes[1, 2].set_xlabel('sepal_width')
    axes[1, 2].set_ylabel('petal_length')

    axes[1, 3].scatter(x=[iris.sepal_width for iris in data], y=[iris.petal_width for iris in data],
                       c=[get_color(iris.iris_class) for iris in data])
    axes[1, 3].set_xlabel('sepal_width')
    axes[1, 3].set_ylabel('petal_width')

    axes[2, 3].scatter(x=[iris.petal_length for iris in data], y=[iris.petal_width for iris in data],
                       c=[get_color(iris.iris_class) for iris in data])
    axes[2, 3].set_xlabel('petal_length')
    axes[2, 3].set_ylabel('petal_width')

    axes[1, 0].scatter(x=[iris.sepal_length for iris in norm_data], y=[iris.sepal_width for iris in norm_data],
                       c=[get_color(iris.iris_class) for iris in norm_data])
    axes[1, 0].set_xlabel('sepal_length')
    axes[1, 0].set_ylabel('sepal_width')

    axes[2, 0].scatter(x=[iris.sepal_length for iris in norm_data], y=[iris.petal_length for iris in norm_data],
                       c=[get_color(iris.iris_class) for iris in norm_data])
    axes[2, 0].set_xlabel('sepal_length')
    axes[2, 0].set_ylabel('petal_length')

    axes[2, 1].scatter(x=[iris.sepal_length for iris in norm_data], y=[iris.petal_width for iris in norm_data],
                       c=[get_color(iris.iris_class) for iris in norm_data])
    axes[2, 1].set_xlabel('sepal_length')
    axes[2, 1].set_ylabel('petal_width')

    axes[3, 0].scatter(x=[iris.sepal_width for iris in norm_data], y=[iris.petal_length for iris in norm_data],
                       c=[get_color(iris.iris_class) for iris in norm_data])
    axes[3, 0].set_xlabel('sepal_width')
    axes[3, 0].set_ylabel('petal_length')

    axes[3, 1].scatter(x=[iris.sepal_width for iris in norm_data], y=[iris.petal_width for iris in norm_data],
                       c=[get_color(iris.iris_class) for iris in norm_data])
    axes[3, 1].set_xlabel('sepal_width')
    axes[3, 1].set_ylabel('petal_width')

    axes[3, 2].scatter(x=[iris.petal_length for iris in norm_data], y=[iris.petal_width for iris in norm_data],
                       c=[get_color(iris.iris_class) for iris in norm_data])
    axes[3, 2].set_xlabel('petal_length')
    axes[3, 2].set_ylabel('petal_width')

    fig.set_figwidth(16)
    fig.set_figheight(16)

    plt.show()


def get_distance(iris_one, iris_two):
    return math.sqrt(math.pow(iris_one.sepal_length - iris_two.sepal_length, 2) +
                     math.pow(iris_one.sepal_width - iris_two.sepal_width, 2) +
                     math.pow(iris_one.petal_length - iris_two.petal_length, 2) +
                     math.pow(iris_one.petal_width - iris_two.petal_width, 2))


def get_optimal_k(data):
    min_k = int(math.sqrt(len(data)) / 2)
    max_k = int(math.sqrt(len(data)) * 2)

    test_data = []
    for i in range(int(len(data) * 0.3)):
        test_data.append(data.pop(0))

    accuracy_on_k = []

    for k in range(min_k, max_k + 1):
        total_count = 0
        correct_count = 0

        for test_item in test_data:
            # Ищем k ближайших соседей
            distance_and_class = []
            for item in data:
                if len(distance_and_class) < k:
                    distance_and_class.append((get_distance(test_item, item), item.iris_class))
                else:
                    max_distance_and_class_index = -1
                    max_distance_and_class = distance_and_class[0]
                    for i in range(len(distance_and_class)):
                        if distance_and_class[i][0] > max_distance_and_class[0]:
                            max_distance_and_class = distance_and_class[i]
                            max_distance_and_class_index = i

                    current_distance = get_distance(test_item, item)
                    if current_distance < max_distance_and_class[0]:
                        distance_and_class[max_distance_and_class_index] = (current_distance,
                                                                            item.iris_class)

            predicted_class = IrisClass.IrisSetosa
            verginica_count = 0
            setosa_count = 0
            versicolour = 0
            for item in distance_and_class:
                if item[1] == IrisClass.IrisVerginica.value:
                    verginica_count += 1
                elif item[1] == IrisClass.IrisSetosa.value:
                    setosa_count += 1
                else:
                    versicolour += 1

            if verginica_count >= setosa_count and verginica_count >= versicolour:
                predicted_class = IrisClass.IrisVerginica
            elif setosa_count >= verginica_count and setosa_count >= versicolour:
                predicted_class = IrisClass.IrisSetosa
            else:
                predicted_class = IrisClass.IrisVersicolour

            if predicted_class.value == test_item.iris_class:
                correct_count += 1
            total_count += 1

        accuracy_on_k.append((correct_count / total_count, k))

    max_accuracy = accuracy_on_k[0]
    for item in accuracy_on_k:
        if item[0] > max_accuracy[0]:
            max_accuracy = item

    return max_accuracy[1]


def classify_iris(min, max, data, k):
    sepal_length = (float(input('Введите sepal_length')) - min[0]) / (max[0] - min[0])
    sepal_width = (float(input('Введите sepal_width')) - min[1]) / (max[1] - min[1])
    petal_length = (float(input('Введите petal_length')) - min[2]) / (max[2] - min[2])
    petal_width = (float(input('Введите petal_width')) - min[3]) / (max[3] - min[3])
    iris = Iris(sepal_length, sepal_width, petal_length, petal_width, IrisClass.IrisVersicolour)

    distance_and_class = []
    for item in data:
        if len(distance_and_class) < k:
            distance_and_class.append((get_distance(iris, item), item.iris_class))
        else:
            max_distance_and_class_index = -1
            max_distance_and_class = distance_and_class[0]
            for i in range(len(distance_and_class)):
                if distance_and_class[i][0] > max_distance_and_class[0]:
                    max_distance_and_class = distance_and_class[i]
                    max_distance_and_class_index = i

            current_distance = get_distance(iris, item)
            if current_distance < max_distance_and_class[0]:
                distance_and_class[max_distance_and_class_index] = (current_distance,
                                                                    item.iris_class)

    verginica_count = 0
    setosa_count = 0
    versicolour = 0
    for item in distance_and_class:
        if item[1] == IrisClass.IrisVerginica.value:
            verginica_count += 1
        elif item[1] == IrisClass.IrisSetosa.value:
            setosa_count += 1
        else:
            versicolour += 1

    if verginica_count >= setosa_count and verginica_count >= versicolour:
        print('Наиболее подходящий вариант: verginica')
    elif setosa_count >= verginica_count and setosa_count >= versicolour:
        print('Наиболее подходящий вариант: setosa')
    else:
        print('Наиболее подходящий вариант: versicolour')

data = load_data()
reshafled_data = reshafle_data(data)
min_max_normalized_data = normalize_data(reshafled_data)
print_projections(reshafled_data, min_max_normalized_data[2])
optimal_k = get_optimal_k(min_max_normalized_data[2])
classify_iris(min_max_normalized_data[0], min_max_normalized_data[1], min_max_normalized_data[2], optimal_k)
