# Animal Guessing
*Acknowledgement: Jan Pearce*

We are to design and implement a program that tries to guess what animal the user has in mind by continually asking questions that can only be answered with a "yes" or "no". Each question will guide the program to ask more questions to narrow down the possibilities until it guesses the animal based on user's answers.

A sample game online is <a href="http://www.animalgame.com/play/index.php" target="_blank">here</a>

To start, our program opens a file called data.json that contains the knowledge it will have before starting the game. Because of the binary nature of "yes" or "no," a binary tree is an appropriate data structure in which to store this information. Note that this will be similar to a binary search tree, but not the same because of the following. Each node of the tree contains a question or a guess, and each edge is the branch it travels based on the answer to a question. Note that all non-leaf nodes have two children. Guesses are located in the leaves. Hence, each time you insert in the tree, a leaf node is replaced by a new subtree which will consist of its question and the two answers.

For example, suppose there are two animals, a zebra or a horse. Assuming that horses have only one color, the question to distinguish between the two is "Does the animal have stripes?" Answering "no" would lead the program to conclude it is a horse, but if it received a "yes" from the user, it would conclude that the animal is a zebra.

The file that contains this information could have the following lines:

Question:
Does the animal have stripes?
no
yes

Guess:
Horse

Guess:
Zebra

The keywords "Question:" and "Guess:" are used as a way to indicate to the program what information follows, but you do not need to do that if you have another method. Note that when using this file format, the program will be building the tree using a preorder traversal, as explained below:

   1. The first thing input from the file is the "Question:" string, which indicates that it is an internal node with two branches; the one to the left is for a "no" response, and the right for a "yes" response.

   2. Because you will be are creating the tree from left to right, the next entry is for the left child (the one for the "no" response") of the node you just created. It is a guess, as indicated by the "Guess:" string, so it is a leaf node (i.e. it has no children) with the value "Horse". You will stop building this branch of the binary tree.

   3. The next entry, "Guess:" with "Zebra" is the right child of the "Question:" node which is the guess if the user answered "yes" to the question. It is also a leaf node, so after you create it,  stop.

   4. When you reach the end of the file, so stop processing and have the information stored in a binary tree, visually represented as the following image: Animal guessing node, with a yes leading to the right and a no answer to 'does it have stripes' leading to the left.
    
![alt text](http://cs.berea.edu/courses/csc236/images/AnimalGuessing1.jpg)

A more sophisticated program may have more layers on this tree and more questions as a result of how the user answered a question. Suppose that it first asks whether it has hooves. Based on the user's answer and its internal storage, it either guesses that the animal is an elephant, which does not have hooves, or asks a question to narrow down which hooved animal he/she had in mind.

You can find the following file a18game.txt  in the A18-AnimalGuessing repository which you should clone:

Question:
Does the animal have hooves?
no
yes

Guess:
Elephant

Question:
Does the animal have stripes?
no
yes

Guess:
Horse

Guess:
Zebra

The tree that contains this information would look like:

![alt text](http://cs.berea.edu/courses/csc236/images/AnimalGuessing2.jpg)

A more complex tree storing information about animals

You may assume that the file your program will input is in the correct format.

Once the program loads this information, it would start asking the user questions starting from the root until it makes a guess as to what the animal is. Once it makes a guess, the program does one of two things:

   1. If the guess is correct, the program asks the user to play again, and starts over if the user answers yes. If the user selects to quit, your program saves its knowledge into a file a18game.txt and then ends.

   2. If the guess is incorrect, it would prompt the user for what the correct answer is and the question that would distinguish the correct from the incorrect guess. Using this information, the program will update its data structure so that the next time, it will the question and makes the correct guess. In other words, it can LEARN!
    The program then asks the user if she/he would like to play again. As in the case above, it either restarts from the question at the root of the tree if the user answers yes or saves its knowledge in a18game.txt before ending.


