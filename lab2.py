import numpy as np

losses = [300, 100, 200, 400]  
probabilities = [0.2, 0.3, 0.1, 0.4]  

expected_loss = np.dot(losses, probabilities)

variance = np.dot([(x - expected_loss) ** 2 for x in losses], probabilities)
std_deviation = np.sqrt(variance)

coefficient_of_variation = std_deviation / expected_loss

max_loss = max(losses)

print(f"Очікувані збитки: {expected_loss} грош. од.")
print(f"Дисперсія: {variance} грош. од.")
print(f"Середньоквадратичне відхилення: {std_deviation} грош. од.")
print(f"Коефіцієнт варіації: {coefficient_of_variation}")
print(f"Максимальний можливий збиток: {max_loss} грош. од.")
