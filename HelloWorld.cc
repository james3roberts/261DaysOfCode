// //Test for c++
// #include <iostream>

// int main () {
// 	std::cout <<"Hello World!";
// 	return 0;
// }


//Starter code for a simple game tetris
//will need to move to a new file
#include <iostream>
using namespace std;
// figure out what a wstring is
wstring tetromino[7];
int main(){
	//create the blocks first
	//this should make it 4 blocks tall and 4 blocks wide
	//Making the blocks in a string so I can see what they are 
	tetromino[0].append(L"..x.");
	tetromino[0].append(L"..x.");
	tetromino[0].append(L"..x.");
	tetromino[0].append(L"..x.");
	//create 2nd block
	tetromino[1].append(L"..x.");
	tetromino[1].append(L".xx.");
	tetromino[1].append(L".x..");
	tetromino[1].append(L"....");
	//create 3rd block
	tetromino[2].append(L".x..");
	tetromino[2].append(L".xx.");
	tetromino[2].append(L"..x.");
	tetromino[2].append(L"....");
	//4th block
	tetromino[3].append(L"....");
	tetromino[3].append(L".xx.");
	tetromino[3].append(L".xx.");
	tetromino[3].append(L"....");
	//time 3:11 should show what all of the shaper are when finished. 

	return 0;
}