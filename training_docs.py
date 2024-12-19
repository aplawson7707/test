import os

def combine_files():
    """
    Combine .txt files from specific directories into two output files:
    yvs_training.txt and mra_training.txt.
    """
    # Hardcoded directories
    yvs_chatbot_dir = os.path.expanduser("~/projects/test/yvs_chatbot")
    mra_chatbot_dir = os.path.expanduser("~/projects/test/mra_chatbot")
    all_chatbots_dir = os.path.expanduser("~/projects/test/all_chatbots")

    # Output file paths
    yvs_output = os.path.expanduser("~/projects/test/yvs_training.txt")
    mra_output = os.path.expanduser("~/projects/test/mra_training.txt")

    try:
        # Helper function to collect .txt files from a directory
        def collect_txt_files(directory):
            contents = []
            for file_name in os.listdir(directory):
                if file_name.endswith('.txt'):
                    file_path = os.path.join(directory, file_name)
                    with open(file_path, 'r') as infile:
                        contents.append(f"--- {file_name} ---\n")
                        contents.append(infile.read())
                        contents.append(f"\n\n")
            return contents

        # Collect contents for yvs_training.txt
        yvs_contents = collect_txt_files(yvs_chatbot_dir) + collect_txt_files(all_chatbots_dir)

        # Collect contents for mra_training.txt
        mra_contents = collect_txt_files(mra_chatbot_dir) + collect_txt_files(all_chatbots_dir)

        # Write to output files
        with open(yvs_output, 'w') as yvs_file:
            yvs_file.writelines(yvs_contents)
        print(f"yvs_training.txt created at {yvs_output}")

        with open(mra_output, 'w') as mra_file:
            mra_file.writelines(mra_contents)
        print(f"mra_training.txt created at {mra_output}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
combine_files()

