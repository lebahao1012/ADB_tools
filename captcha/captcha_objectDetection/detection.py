import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

class YOLOVisualizer:
    def __init__(self, output, img):
        self.output = output
        self.img = img

    def checking_matching(self, labels):
        locations = []
        for i in range(len(labels)):
            for j in range(i + 1, len(labels)):
                if labels[i] == labels[j]:
                    print("Hai ký tự giống nhau là:", labels[i])
                    locations.append(i)
                    locations.append(j)
        return locations
    
    def random_coordinate_in_bbox(self, x, y, width, height):
        random_x = random.uniform(x, x + width)
        random_y = random.uniform(y, y + height)
        return random_x, random_y

    def visualize_matching_boxes(self):
        results = self.output.predict(source=self.img)
        a = results[0].boxes.data
        labels = []
        names = self.output.names
        for r in results:
            for c in r.boxes.cls:
                labels.append(names[int(c)])

        matching = self.checking_matching(labels)
        
        matching_points = []

        xmin = [box[0].item() for box in a]
        ymin = [box[1].item() for box in a]
        xmax = [box[2].item() for box in a]
        ymax = [box[3].item() for box in a]

        plt.imshow(self.img)

        num1 = matching[0]
        xmin_matching1 = xmin[num1]
        ymin_matching1 = ymin[num1]
        xmax_matching1 = xmax[num1]
        ymax_matching1 = ymax[num1]

        bbox = patches.Rectangle((xmin_matching1, ymin_matching1), xmax_matching1 - xmin_matching1, ymax_matching1 - ymin_matching1, linewidth=1, edgecolor='r', facecolor='none')
        plt.gca().add_patch(bbox)
        matching_points.append(((xmin_matching1, ymin_matching1), xmax_matching1 - xmin_matching1, ymax_matching1 - ymin_matching1))
        random_point1 = self.random_coordinate_in_bbox(xmin_matching1, ymin_matching1, xmax_matching1 - xmin_matching1, ymax_matching1 - ymin_matching1)
        print("Random point 1 within the bounding box:", random_point1)
        plt.scatter(random_point1[0], random_point1[1], color='red', label='Point 1')

        num2 = matching[1]
        xmin_matching2 = xmin[num2]
        ymin_matching2 = ymin[num2]
        xmax_matching2 = xmax[num2]
        ymax_matching2 = ymax[num2]

        bbox = patches.Rectangle((xmin_matching2, ymin_matching2), xmax_matching2 - xmin_matching2, ymax_matching2 - ymin_matching2, linewidth=1, edgecolor='r', facecolor='none')
        plt.gca().add_patch(bbox)
        matching_points.append(((xmin_matching2, ymin_matching2), xmax_matching2 - xmin_matching2, ymax_matching2 - ymin_matching2))
        random_point2 = self.random_coordinate_in_bbox(xmin_matching2, ymin_matching2, xmax_matching2 - xmin_matching2, ymax_matching2 - ymin_matching2)
        print("Random point 2 within the bounding box:", random_point2)
        plt.scatter(random_point2[0], random_point2[1], color='blue', label='Point 2')

        plt.legend()

        print("2 bounding boxes:",matching_points)
        plt.show()
