import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


#example 1
# plt.figure(figsize=(8,6))
# plt.scatter(1, 3, marker='o')
# plt.scatter(2, 10, marker='o')
# plt.scatter(3, 7, marker='o')
# plt.scatter(4,15, marker='o')
# plt.xlabel('Days')
# plt.ylabel('Number of Birds')
# plt.title("State Park Bird Counts")
# plt.grid(True)
# plt.show()

#example 2
# plt.figure(figsize=(8,6))
# t = np.linspace(0,1,101) #creating 11 points from 0-10
# w = 2 * np.pi * 3
# sin_fn= np.sin(w*t)
# plt.plot(t, sin_fn)
# plt.show()

# Example 3
# fig, axes = plt.subplots(2, 2, figsize=(10,8))

# t = np.linspace(0,1, 101)
# sinfn1 = np.sin(2 * np.pi * 1 * t)
# sinfn2 = np.sin(2 * np.pi * 2 * t)
# sinfn3 = np.sin(2 * np.pi * 3 * t)
# sinfn4 = np.sin(2 * np.pi * 4 * t)
#
# axes[0,0].plot(t, sinfn1)
# axes[0,0].set_xlabel('time(sec)')
# axes[0,0].set_ylabel('sin function - 1 Hz')
#
# axes[0,1].plot(t, sinfn2)
# axes[0,1].set_xlabel('time(sec)')
# axes[0,1].set_ylabel('sin function - 2 Hz')
#
# axes[1,0].plot(t, sinfn3)
# axes[1,0].set_xlabel('time(sec)')
# axes[1,0].set_ylabel('sin function - 3 Hz')
#
# axes[1,1].plot(t, sinfn4)
# axes[1,1].set_xlabel('time(sec)')
# axes[1,1].set_ylabel('sin function - 4 Hz')
#
# plt.show()

data = np.array([
    [152, 39, 0],
    [159, 46, 0],
    [144, 41, 0],
    [160, 51, 0],
    [150, 53, 0],
    [156, 38, 0],
    [162, 59, 0],
    [148, 50, 0],
    [161, 42, 0],
    [149, 55, 0],
    [167, 53, 1],
    [173, 66, 1],
    [155, 63, 1],
    [169, 58, 1],
    [176, 47, 1],
    [171, 60, 1],
    [179, 51, 1],
    [157, 70, 1],
    [163, 55, 1],
    [177, 68, 1],
])

our_test_pt = np.array([[115,50]])

#separate features and labels
# height = data[:,0]
# weight = data[:,1]
# labels = data[:,2]
#
# plt.figure(figsize=(8,6))
# plt.scatter(height[labels == 0], weight[labels == 0], label='8th grade', marker='o')
# plt.scatter(height[labels == 1], weight[labels == 1], label='10th grade', marker='s')
# plt.xlabel('Height (cm)')
# plt.ylabel('Weight (kg)')
# plt.title('Student Height vs Weight')
# plt.legend()
# plt.grid(True)
# plt.show()


#sklearn and random forest
#split features and labels
X = data[:, :2] #height and weight
y = data[:, 2] #label (grade)

for i in range(10):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

h = X_scaled[:,0]
w = X_scaled[:,1]

#plotting normalized data
plt.figure(figsize=(8,6))
plt.scatter(h[y == 0], w[y == 0], label='8th grade', marker='o')
plt.scatter(h[y == 1], w[y == 1], label='10th grade', marker='s')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Student Height vs Weight')
plt.legend()
plt.grid(True)
plt.show()

#split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

#train a random forest classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

#predict on the test set
y_pred = model.predict(X_test)

#evaluate accuracy
print('Accuracy:', accuracy_score(y_test, y_pred)) #accuracy: 1.0 (100%)
