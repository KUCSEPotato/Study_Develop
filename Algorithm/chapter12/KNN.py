# Example of KNN
import numpy as np
from collections import Counter

def euclidean_distance(point1, point2):
    """Compute the Euclidean distance between two points."""
    return np.sqrt(np.sum((point1 - point2) ** 2))

def knn_classifier(train_data, train_labels, test_data, k=3):
    """Classify test data using the k-Nearest Neighbors algorithm."""
    predictions = []
    for test_point in test_data:
        # Compute distances from the test point to all training points
        distances = [euclidean_distance(test_point, train_point) for train_point in train_data]
        
        # Get the indices of the k nearest neighbors
        k_indices = np.argsort(distances)[:k]
        
        # Extract the labels of the k nearest neighbors
        k_nearest_labels = [train_labels[i] for i in k_indices]
        
        # Determine the most common class label among the neighbors
        most_common = Counter(k_nearest_labels).most_common(1)
        predictions.append(most_common[0][0])
    
    return np.array(predictions)

def main():
    # Sample training data (features and labels)
    train_data = np.array([[1, 2], [2, 3], [3, 1], [6, 5], [7, 7], [8, 6]])
    train_labels = np.array(['A', 'A', 'A', 'B', 'B', 'B'])
    
    # Sample test data
    test_data = np.array([[2, 2], [6, 6]])
    
    # Classify test data
    k = 3
    predictions = knn_classifier(train_data, train_labels, test_data, k)
    
    print("Predictions for test data:", predictions)

if __name__ == "__main__":
    main()