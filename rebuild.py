import os

# Config
HEADER = b"BURIKO ARC20"  # BGI/Ethornell's .arc files always start with this header in bytes.
HEADER_SIZE = 12
FILE_ENTRY_SIZE = 128  # 96 (name) + 4 (offset) + 4 (size) + 24 (padding)
extracted_directory = "extracted"

# Create the .arc file
def create_arc(input_files, output_file):
    offsets = []
    sizes = []
    data_offset = 0

    with open(output_file, "wb") as arc_file:
        """
        Write Header
        """
        arc_file.write(HEADER)  # "BURIKO ARC20" as the header
        arc_file.write(len(input_files).to_bytes(4, "little"))  # File count

        """
        Create Index
        """
        for file_path in input_files:
            file_name = os.path.basename(file_path)

            """
            with open(file_path, "rb") as f:
                raw_data = f.read()
                compressed_data = compress(raw_data)

            file_size = len(compressed_data)
            """
            file_size = os.path.getsize(file_path)

            # Save name with padding
            name_encoded = file_name.encode("shift_jis")[:96]  # Truncate if too long
            name_padded = name_encoded + b"\x00" * (96 - len(name_encoded))
            arc_file.write(name_padded)

            # Save offset and size
            arc_file.write(data_offset.to_bytes(4, "little"))
            arc_file.write(file_size.to_bytes(4, "little"))

            # Save extra padding (24 bytes)
            arc_file.write(b"\x00" * 24)

            # Register offset and size
            offsets.append(data_offset)
            sizes.append(file_size)

            # Update the next offset
            data_offset += file_size

        """
        Writing data
        """
        for file_path in input_files:
            with open(file_path, "rb") as f:
                raw_data = f.read()
                arc_file.write(raw_data)
            print(f"File added: {file_path}")

    print(f"File created: {output_file}")


def process_folder():
    # Making sure the 'extracted' folder exists.
    if not os.path.exists(extracted_directory):
        os.makedirs(extracted_directory)
        print(f"'{extracted_directory}' folder created.")
        print("Make sub-folders with files or drop some extension-less files in there and run this script again.")
        #print("^^ and make sure you ALWAYS have the original .arc in the same folder as this script.")
        print("(If you create folders with files, name it the same as the original .arc file without the extension)")
        return

    # Extension-less files in 'extracted'
    root_files = [
        os.path.join(extracted_directory, f)
        for f in os.listdir(extracted_directory)
        if os.path.isfile(os.path.join(extracted_directory, f)) and "." not in f
    ]

    # Sub-folders in 'extracted'
    subfolders = [
        os.path.join(extracted_directory, f)
        for f in os.listdir(extracted_directory)
        if os.path.isdir(os.path.join(extracted_directory, f))
    ]

    # Extension-less files without a sub-folder
    if root_files:
        arc_files = [
            f for f in os.listdir() if os.path.isfile(f) and f.endswith(".arc")
        ]
        if not arc_files:
            raise FileNotFoundError("You need the original .arc file to be in the same directory as this script.")

        arc_name = os.path.splitext(arc_files[0])[0] + ".arc.new"
        create_arc(root_files, arc_name)

    # Sub-folders with extension-less files
    elif subfolders:
        for subfolder in subfolders:
            folder_name = os.path.basename(subfolder)
            subfolder_files = [
                os.path.join(subfolder, f)
                for f in os.listdir(subfolder)
                if os.path.isfile(os.path.join(subfolder, f)) and "." not in f
            ]

            if not subfolder_files:
                raise FileNotFoundError(
                    f"The sub-folder '{folder_name}' didn't have any extension-less files to process."
                )

            arc_name = f"{folder_name}.arc.new"
            create_arc(subfolder_files, arc_name)
    else:
        raise FileNotFoundError(
            "No extension-less files or no sub-folders with extension-less files to process found in the 'extracted' folder."
        )


process_folder()
