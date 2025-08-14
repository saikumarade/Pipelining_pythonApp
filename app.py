from model import train_model
import numpy as np

# Train the model
model = train_model()

def main():
    print("Simple Sum Prediction (no Flask)")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        input_data = np.array([[num1, num2]])
        prediction = model.predict(input_data, verbose=0)
        print(f"Predicted Sum: {prediction[0][0]:.2f}")
    except Exception as e:
        print("Invalid input. Please enter valid numbers.")
        print("Error:", e)

if __name__ == "__main__":
    main()


