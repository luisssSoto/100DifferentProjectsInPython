sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = sentence.split()
result = {word:len(word) for word in result}
print(result)
