# Allows creation of directories
import os


# Each website crawled is a new project
# create dir if it doesn't exist
def create_project_dir(base_url):
    # Get the directory where the script is located
    directory = os.path.dirname(os.path.realpath(__file__))
    # Join the website domain and the directory to create a subdir with website name
    directory = os.path.join(directory, base_url.replace('http://', '').replace('https://', '').replace('.', '_').replace(':', '_'))
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)
    print(os.path.exists(directory))
    return directory

# Create queue and crawled files
def create_data_files(path, base_url):
    queue = path + '/queue.txt'
    crawled = path + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Creates a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# Delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        #does nothing(clears the file)
        pass

# Read a file and convert each line to set items and removes the \n
def file_to_set(file_name):
    results = set()
    #rt - read text file
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
        return results


# Iterate throught a set, each item in a set will be a new line in the file
def set_to_file(links, file):
    #removes the old data because a new crawler call has been made
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)

path = create_project_dir('http://thought.edge.com')
create_data_files(path, 'https://thought.edge.com')
