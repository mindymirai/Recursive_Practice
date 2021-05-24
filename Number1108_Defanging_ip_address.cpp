class Solution {
public:
    string defangIPaddr(string address) {
        if (address.size()==0){
            return "";
        }
        string head = address.substr(0, address.size()-1); 
        /* take legnth*/
        string tail = {address.back()};
        if(tail == "."){
            return defangIPaddr(head) + "[.]";
        }else{
            return defangIPaddr(head) + tail;
        }   
    }        
};