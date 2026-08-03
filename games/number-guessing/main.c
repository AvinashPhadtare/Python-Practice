#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    srand(time(0)); // game of gussing
    char name1[50];
    printf("Enter FIRST player name :");
    scanf("%s",name1);
    char name2[50];
    printf("Enter SECOND player name:");
    scanf("%s",name2);
    int randomnumber1 = (rand() % 100) + 1;
    int randomnumber2 = (rand() % 100) + 1;
    int no_of_guesses1 = 0;
    int no_of_guesses2 = 0;
    int guessed;

    printf("\n");
    printf("TURN OF FIRST PLAYER\n");
    do
    {
        printf("Guess the number :  ");
        scanf("%d", &guessed);
        if (guessed > randomnumber1)
        {
            printf("Lower number please!\n");
        }
        else if (guessed < randomnumber1)
        {
            printf("Higher number please!\n");
        }
        else
        {
            printf("Congrates!!..\n");
        }
        no_of_guesses1++;
    } while (guessed != randomnumber1);

    printf("\n");
    



    printf("TURN OF SECOND PLAYER\n");
    do
    {
        printf("Guess the number :  ");
        scanf("%d", &guessed);
        if (guessed > randomnumber2)
        {
            printf("Lower number please!\n");
        }
        else if (guessed < randomnumber2)
        {
            printf("Higher number please!\n");
        }
        else
        {
            printf("Congrates!!..\n");
        }
        no_of_guesses2++;
    } while (guessed != randomnumber2);
    
    printf("\n");


    if (no_of_guesses1 < no_of_guesses2)
    {
        printf("%s guessed the number in %d guesses\n",name1, no_of_guesses1);
        printf("%s is winer of the game",name1);
    }
    else if (no_of_guesses1 > no_of_guesses2)
    {
        printf("%s guessed the number in %d guesses\n",name2, no_of_guesses2);
        printf("%s is winer of the game",name2);
    }
    else if (no_of_guesses1 == no_of_guesses2)
    {
        printf("It's a TIE !...\n");
        printf("Better luck next time ! :(\n");
        
    }
    
    
    return 0;
}
