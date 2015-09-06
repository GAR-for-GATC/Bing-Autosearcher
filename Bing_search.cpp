//This program types "www.bing.com", then presses the "enter" key
/////////////////////////////////////////////////////////////////

//To compile using gcc, use a command similar to:
// g++ Bing_search.cpp -I/pdf_stuff/test_header.h -o test_file.exe


// Windows key code references:
//https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731%28v=vs.85%29.aspx
#define WINVER 0x0500
#include <windows.h>
#include <iostream>
//#include <map>
#include <ctime> 
#include <stdlib.h>//For random number
#include "Word_Bank.h"
using namespace std;
void type_word(string word);
//   This function presses a button based on the windows key value
//passed to it in hex format.
void press_button(int butt_hex)

{
	INPUT my_butt;
	my_butt.type = INPUT_KEYBOARD;
	my_butt.ki.wScan = 0;
	my_butt.ki.time = 0;
	my_butt.ki.dwExtraInfo = 0;
	
	my_butt.ki.wVk = butt_hex;  //Key-code key
	my_butt.ki.dwFlags = 0;
	SendInput(1, &my_butt, sizeof(INPUT)); //Press key down
	my_butt.ki.dwFlags = KEYEVENTF_KEYUP; 
    SendInput(1, &my_butt, sizeof(INPUT)); //Un-press key
}
//This word bank is full of terms to search for.
string small_word_bank[31] = {"purple","flower","cake","portal", "ai","maroon","green","black","grey",
	"fuchia","finger","cat","dog","fish","turquoise","grey","cute","lamp","rush","rabbit",
	"squirrel","teapot","blanket","cube","square","lock","key","silly","pillow","hands", "reddit"};

int main()
{
	
	Sleep(5000);
	srand(time(NULL));//makes rand random
	int w=0x57; //W key
	int period = 0x6E;
	int b = 0x42;
	int i = 0x49;
	int n = 0x4E;
	int g = 0x47;
	int c = 0x43;
	int o = 0x4F;
	int m = 0x4D;
	int enter = 0x0D;
	int backspace = 0x08;

		
	press_button(w);
	press_button(w);
	press_button(w);
	press_button(period);
	press_button(b);
	press_button(i);
	press_button(n);
	press_button(g);
	press_button(period);
	press_button(c);
	press_button(o);
	press_button(m);
	press_button(enter);
	Sleep(1500);

	for (int apple=0; apple<40;apple++)
	{
		int number_one = rand()%200+1500; //random number from 1500 to 1699
		int number_two = rand()%260+1000;
		string idk_string = large_word_bank();
		type_word(idk_string);
		press_button(enter);
		Sleep(number_one);
		press_button(backspace);
		Sleep(number_two);
	}
	cin.get();
	return 0;

}

//This function types a word taken from word bank

void type_word(string word)
{
	int key_array[26]{0x41,0x42,0x43,0x44,0x45,0x46,0x47,0x48,0x49,0x4A,0x4B,0x4C,
		0x4D, 0x4E,0x4F,0x50,0x51,0x52,0x53,0x54,0x55,0x56,0x57,0x58,0x59,0x5A};
	
	//Value in double quotes is a null-terminated string; an array of characters.
	//Value in single quotes is a char.
	char char_array[26]{'a','b','c','d','e','f','g','h','i','j','k','l','m','n',
		'o','p','q','r','s','t','u','v','w','x','y','z'};
	int the_key;
	for(int my_int= 0;my_int<word.length();my_int++)
	{

		char my_char = word[my_int];
		
		//Finds the the microsoft key for the letter
		//Loop through char_arry to find the one that's equivalent.
		//Find the position of that element.
		//make the_key equal to the same position in key_array
		for(int x=0; x<30;x++)
		{
			if (my_char == char_array[x])
			{
				the_key = key_array[x];
				press_button(the_key);
			}
						
		}
	}
}




