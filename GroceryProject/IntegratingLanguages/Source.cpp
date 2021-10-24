#include "Python.h"
#include <iostream>
#include "Functions.h"
#include <cmath>
#include <string>
#include <cstdio>
#include <limits>

using namespace std;

void main() {

	string name;
	int userChoice;

	// menus option
	do {
		cout << "1: A List of All Items Purchased in a Given Day\n";
		cout << "2: A Number representing Times a Specific Item was Purchased\n";
		cout << "3: A Text-based Histogram \n";
		cout << "4: Exit\n";
		cout << "Enter your selection as a number 1, 2, 3 or 4.\n";

		if (cin >> userChoice)	{

			switch (userChoice) {

			case 1:
				cout << "Produce a list of all items purchased in a given day along with the number of times each item was purchased. \n";

				cout << "\n";
				CallProcedure("freq"); // frequency function	
				cout << "\n";
				break;

			case 2:
				cout << "Produce a number representing how many times a specific item was purchased in a given day. \n";
				cout << "Please Enter an Item to Search: ";
				cin >> name;
				cout << "\n";
				cout << "The frequency of the " << name << " is : " << callIntFunc("frequency", name) << endl; // call the frequency function
				cout << "\n";
				break;

			case 3:
				cout << "Produce a text-based histogram listing all items purchased in a given day, & their frequency.";
				cout << "\n";
				CallProcedure("histogram");// histogram function	
				cout << "\n";
				break;

			case 4:
				cout << "Thank you";
				break;

			default:
				cout << "Invalid Option, Try again" << endl;
				break;
			}
		}

		else	{
			// Error message
			cout << "You entered non integer characters" << endl;
			break;
		}
	} while (userChoice != 4);

	(void)getchar();

}
