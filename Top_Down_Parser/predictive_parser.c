#include <math.h>
#include <stdio.h>

char *lookahead;
int aux=0;
char string[]= "array";

void primitive(){
    if(lookahead == "integer" || lookahead == "char"){
        recognize(lookahead);
    } else if(lookahead == "num"){
        recognize("num");
        recognize("..");
        recognize("num");
    } else{
        erro();
    }

}

void type(){
    if(lookahead =="↑"){
        recognize("↑");
        recognize("id");
    } else if(lookahead == "array"){
        recognize("array");
        recognize("[");
        primitive();
        recognize("]");
        recognize("of");
        type();
    } else{
        primitive();
    }
}

void recognize(char token[]){
    if(token == lookahead){
        lookahead = nextToken();
    } else{
        erro();
    }
}

int main(){
    return 0;
}