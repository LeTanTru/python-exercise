from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.datasets import load_iris

# Load dữ liệu Iris
iris = load_iris()
X = iris.data
y = iris.target

# Chia tập dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Xây dựng mô hình KNN
knn_model = KNeighborsClassifier(n_neighbors=5)

# Huấn luyện mô hình
knn_model.fit(X_train, y_train)

# Dự đoán nhãn của tập kiểm tra
y_pred = knn_model.predict(X_test)

# Đánh giá mô hình
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average="weighted")
precision = precision_score(y_test, y_pred, average="weighted")
recall = recall_score(y_test, y_pred, average="weighted")

print("Accuracy:", accuracy)
print("F1-score:", f1)
print("Precision:", precision)
print("Recall:", recall)


print("Nhãn dự đoán của tập kiểm tra:")
print(y_pred)

print("\nGiá trị thực tế:")
print(y_test)

target_names = iris.target_names

predicted_species = [target_names[i] for i in y_pred]
print("\nTên loài dự đoán:")
print(predicted_species)

actual_species = [target_names[i] for i in y_test]
print("\nTên loài thực tế:")
print(actual_species)
