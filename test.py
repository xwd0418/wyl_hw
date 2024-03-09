import subprocess

def test_java(test_txt_file_path, java_class_name):
        
        
    # Compile the Java code
    subprocess.run(["javac", f"{java_class_name}.java"])

    # Read inputs and expected outputs from a.txt
    with open(test_txt_file_path, "r") as file:
        lines = file.readlines()

    # Split the lines into inputs and expected outputs
    inputs = []
    expected_outputs = []
    for i, line in enumerate(lines):
        if i % 2 == 0:
            inputs.append(line.strip())
        else:
            expected_outputs.append(line.strip())

    # Run the Java code with inputs from a.txt
    actual_outputs = []
    for input_data in inputs:
        process = subprocess.Popen(["java", f"{java_class_name}"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        output, _ = process.communicate(input_data)
        actual_outputs.append(output.strip())

    # Compare actual outputs with expected outputs
    for i, (actual_output, expected_output) in enumerate(zip(actual_outputs, expected_outputs)):
        print(f"Test Case {i + 1}:")
        print("Input:", inputs[i])
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)
        if actual_output == expected_output:
            print("Result: Passed")
        else:
            print("Result: Failed")
        print()

    # Remove the compiled class file
    subprocess.run(["rm", f"{java_class_name}.class"])