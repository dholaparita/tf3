import re

def generate_output_file(tf_filename, output_filename):
    # Initialize an empty list to hold the names of the buckets
    resource_names = []

    # Try to open and read the main.tf file line by line
    try:
        with open(tf_filename, 'r', encoding='utf-8') as file:
            # Read the file line by line
            for line in file:
                # Use a regular expression to match resource names
                match = re.search(r'resource "aws_s3_bucket" "([\w-]+)"', line)
                if match:
                    # If a match is found, add the resource name to the list
                    resource_names.append(match.group(1))

    except FileNotFoundError:
        print(f"The file {tf_filename} was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Generate the content for the output.tf file
    output_content = ""
    for name in resource_names:
        output_content += f'''output "{name}_id" {{
  description = "The ID of the S3 bucket {name}"
  value       = aws_s3_bucket.{name}.id
}}

'''

    # Write the content to the output.tf file
    with open(output_filename, 'w') as file:
        file.write(output_content)
    print(f"File {output_filename} has been created with {len(resource_names)} outputs.")

# Call the function with the filenames
generate_output_file('main.tf', 'output.tf')
