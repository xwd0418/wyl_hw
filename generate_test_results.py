import subprocess


def generate_java_test(save_path, java_class_name):
    # Compile the Java code
    subprocess.run(["javac", f"{java_class_name}.java"])

    # Run the Java code with each input and capture the outputs
    actual_outputs = []
    with open(save_path, "r") as file:
        test_inputs = file.readlines()

    for input_data_raw in test_inputs:
        input_data = input_data_raw.strip()
        process = subprocess.Popen(["java", f"{java_class_name}"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        output, _ = process.communicate(input_data)
        actual_outputs.append(output.strip())

    # Write inputs and expected outputs to a.txt
    with open(save_path, "w") as file:
        for input_data, actual_output in zip(test_inputs, actual_outputs):
            file.write(input_data + "\n")
            file.write(actual_output + "\n")

    # Remove the compiled class file
    subprocess.run(["rm", f"{java_class_name}.class"])

# main 
if __name__ == "__main__":
    generate_java_test("Q1.txt", "Q1Substring")
    print("Test results saved to a.txt")