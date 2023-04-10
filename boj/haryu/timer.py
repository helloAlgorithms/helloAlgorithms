import time
import subprocess
start_time = time.time()

## source code 
file_path = "/home/haryu/helloAlgorithms/boj/haryu/18108.py"
subprocess.run(["python3", file_path])

end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_formmated = round(elapsed_time, 2);
print("Code Processed : ", elapsed_time_formmated, "sec")