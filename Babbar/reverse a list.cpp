
void swap(char *a, char *b){
    char *t;
    t = a;a = b;b=t;
}

string reverseWord(string str){
    int n = str.length();
    for(int i = 0; i < n / 2 ; i++){
        swap(str[i],str[n - 1 - i ]);
    }
    return str;
  //Your code here
}