import os

#Each folder hold separated crawl for one website

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)

# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

#Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()