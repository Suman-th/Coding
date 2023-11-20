#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# insert into dictionary
def insert_dict(key, value, dict):
    
    # Your code here
    dict[key] = value

# deleting from dictionary
def del_dict(key, dict):
    if key not in dict:
        return False
    del dict[key]

# print marks of required name
def print_dict(key, dict):
    
    if key not in dict:
        return False
    
    print("Marks of" +" " +key +" " +"is" +" " +dict.get(key))
    
    # Your code here
    
    
    

#{ 
 # Driver Code Starts.
# Driver code
def main():
    # testcase input
    testcase = int(input())
    
    # looping through testcases
    while(testcase > 0):
        
        n = int(input())
        
        i = 0
        dict = {}
        while i < n:
            flag = False
            delete = False
            query = input().split()
            if(query[0] == 'i'):
                insert_dict(query[1], query[2], dict)
                print ("Inserted")
            
            if(query[0] == 'd'):
                if del_dict(query[1], dict) is False:
                    print ("-1")
                else:
                    print ("Deleted")
            
            if(query[0] == 'p'):
                if(print_dict(query[1], dict) is False):
                    print ("-1")
                    
            i+=1
            
        testcase -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends