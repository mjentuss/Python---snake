#include <iostream>
#include <windows.h>
#include <conio.h>
#include <fstream>
#include <vector>
#include "pingpong.h"
using namespace std;

enum enumDir
{
    STOP = 0,
    LEFT = 1,
    UPLEFT = 2,
    DOWNLEFT = 3,
    RIGHT = 4,
    UPRIGHT = 5,
    DOWNRIGHT = 6
};
//----------------------------------------------------------------------------
class Ball
{
    int x, y; //przechowywanie pozycji pilki na ekranie
    int orix, oriy; //zmienne pozycji startowej pilki
    enumDir direction;
public:
    Ball(int orix, int oriy); //konstruktor ustawia aktualne kordy x y na orix oriy
    void reset();
    void changeDir(enumDir);
    int getx()
    {
        return x; 
    }
    int gety()
    {
        return y;
    }
    enumDir getDirection()
    {
        return direction;
    }
    void randDir();
    void Move();
    friend ostream & operator << (ostream &o, Ball c);
};

Ball::Ball(int orix, int oriy)
{
    this->orix=orix;
    this->oriy=oriy;
    this->x=orix;
    this->y=oriy;
    direction = STOP;
}

void Ball::reset()
{
    this->x=orix;
    this->y=oriy;
    direction = STOP;
}

void Ball::changeDir(enumDir d)
{
    direction = d;
}

void Ball::randDir()
{
    direction = (enumDir)((rand() % 6)+1);
}

void Ball::Move() //funkcjonowanie ruchu
{
    switch(direction)
    {
    case STOP:
        break;
    case LEFT:
        x--;
        break;
    case RIGHT:
        x++;
        break;
    case UPLEFT:
        x--;
        y--;
        break;
    case UPRIGHT:
        x++;
        y--;
        break;
    case DOWNLEFT:
        x--;
        y++;
        break;
    case DOWNRIGHT:
        x++;
        y++;
        break;
    default:
        break;
    }
}

ostream & operator << (ostream &o, Ball c)
{
    o << "Ball [" << c.x << "," << c.y << "][" << c.direction << "]";
    return o;
}
//----------------------------------------------------------------------------
class Players
{
    int x, y; // zmienne odp za wspol gracza
    int orix, oriy; //zmienne odp za pierwotne polozenie
public:
    Players();
    Players(int orix, int oriy);
    void reset();
    int getx()
    {
        return x;
    }
    int gety()
    {
        return y;
    }
    void moveUP()
    {
        y--;
    }
    void moveDOWN()
    {
        y++;
    }
    friend ostream & operator << (ostream &o, Players p); //wyswietlanie obiektu
};

Players::Players()
{
    x=y=0;
}

Players::Players(int orix, int oriy)
{
    this->orix=orix;
    this->oriy=oriy;
    this->x=orix;
    this->y=oriy;
}

void Players::reset()
{
    this->x=orix;
    this->y=oriy;
}
ostream & operator << (ostream &o, Players p)
{
    o << "Player [" << p.x << "," << p.y << "]";
    return o;
}
//----------------------------------------------------------------------------
class Manager //odpowiada za zarzadzanie gra
{
    int szerokosc, wysokosc;
    static int score1, score2;
    char up1, down1, up2, down2;

    Ball *ball; //wskaznik do ball aby zainicjowac new
    Players *player1; //wskaznik do gracza 1
    Players *player2; //wskaznik do gracza 2
public:
    Manager(int szerokosc=60, int wysokosc=16); //konstruktor odpowiadajacy za rozmiar mapy
    ~Manager(); //zwolnienie pamieci
    void punktuj(Players *player); //funkcja przydzielajaca punkty
    void plansza();
    void input();
    void logic();
    void run();
    void entry();
    vector<int>vec1;
    vector<int>vec2;
};

int Manager::score1=0;
int Manager::score2=0;
Manager::Manager(int szerokosc, int wysokosc)
{
    this->wysokosc=wysokosc;
    this->szerokosc=szerokosc;
    up1='w';
    down1='s';
    up2=72; //strzalka w gore
    down2=80; //strzalka w dol
    ball = new Ball(szerokosc/2, wysokosc/2); //umieszcza pilke na srodku mapy
    player1 = new Players(1, wysokosc/2); //umieszcza gracza na x=[1], y=polowa mapy
    player2 = new Players(szerokosc-2, wysokosc/2);
}
Manager::~Manager()
{
    delete ball, player1, player2;
}

void Manager::punktuj(Players *player)
{
    if(player == player1)
    {
        score1++;
    }
    else if(player == player2)
    {
        score2++;
    }

    if(score1==3 || score2==3)
    {
        if(score1==3)
            cout << "Gracz 1 wygrywa!" << endl;
        else if(score2==3)
            cout << "Gracz 2 wygrywa!" << endl;
        vec1.push_back(score1);
        vec2.push_back(score2);
        getch();
        score1=0;
        score2=0;
    }

    ball->reset();
    player1->reset();
    player2->reset();
}

void Manager::plansza()
{
    system("cls");

    for(int i=0; i<szerokosc+2; i++)
        cout << "#";
    cout << endl;

    for(int i=0; i<wysokosc; i++)
    {
        for(int j=0; j<szerokosc; j++)
        {
            int ballx = ball->getx();
            int bally = ball->gety();
            int player1x = player1->getx();
            int player1y = player1->gety();
            int player2x = player2->getx();
            int player2y = player2->gety();

            if(j==0)
                cout << "#";
            if(ballx==j && bally==i)
                cout <<"O";
            else if(player1x==j && player1y==i)
                cout << "|";
            else if(player2x==j && player2y==i)
                cout << "|";

            else if(player1x==j && player1y+1==i)
                cout << "|";
            else if(player1x==j && player1y+2==i)
                cout << "|";
            else if(player1x==j && player1y+3==i)
                cout << "|";

            else if(player2x==j && player2y+1==i)
                cout << "|";
            else if(player2x==j && player2y+2==i)
                cout << "|";
            else if(player2x==j && player2y+3==i)
                cout << "|";

            else
                cout << " ";
            if(j==szerokosc-1)
                cout << "#";
        }
        cout << endl;
    }
    for(int i=0; i<szerokosc+2; i++)
        cout << "#";
    cout << endl;
    cout << "Gracz 1: " << score1 << "    " << "Gracz 2: " << score2 << endl;

    cout << "                                             ";
    cout << "TABELA OSTATNICH WYNIKOW" << endl;
    for(int i=0; i<vec1.size(); i++)
    {
        cout << "                                             ";
        cout << "[" << i+1 << "]" << ". " << vec1[i] << " ";
        cout << vec2[i] << endl;
    }
}

void Manager::input()
{
    ball->Move();

    int ballx = ball->getx();
    int bally = ball->gety();
    int player1x = player1->getx();
    int player1y = player1->gety();
    int player2x = player2->getx();
    int player2y = player2->gety();

    if(_kbhit())
    {
        char current = _getch();

        if(current == up1)
            if(player1y>0)
                player1->moveUP();
        if(current == down1)
            if(player1y + 4 < wysokosc)
                player1->moveDOWN();

        if(current == up2)
            if(player2y>0)
                player2->moveUP();
        if(current == down2)
            if(player2y + 4 < wysokosc)
                player2->moveDOWN();

        if(ball->getDirection()==STOP)
            ball->randDir();
    }
}

void Manager::logic()
{
    int ballx = ball->getx();
    int bally = ball->gety();
    int player1x = player1->getx();
    int player1y = player1->gety();
    int player2x = player2->getx();
    int player2y = player2->gety();

    for(int i=0; i<4; i++) //lewa paletka
        if(ballx==player1x+1)
            if(bally==player1y+i)
                ball->changeDir((enumDir)((rand()%3)+4)); //jesli uderzy w lewa paletke, losuje odbicie w prawo enum 4-6

    for(int i=0; i<4; i++) //prawa paletka
        if(ballx==player2x-1) // -1 bo chcemy by pilka odbila sie przed paletka a nie w niej
            if(bally==player2y+i)
                ball->changeDir((enumDir)((rand()%3)+1)); //jesli uderzy w prawa paletke, losuje odbicie w prawo enum 1-3

    if(bally==wysokosc-1) //-1 bo nie chcemy by wpadla w sciane tylko sie od niej odbila
        ball->changeDir(ball->getDirection() == DOWNRIGHT ? UPRIGHT : UPLEFT);

    if(bally==0)
        ball->changeDir(ball->getDirection() == UPRIGHT ? DOWNRIGHT : DOWNLEFT);

    if(ballx==szerokosc-1)
        punktuj(player1);

    if(ballx==0)
        punktuj(player2);
}

void Manager::run()
{

    plansza();
    input();
    logic();
    Sleep(20);
}

void Manager::entry()
{
    string linia;
    fstream plik;
    plik.open("plik.txt", ios::in);
    if(plik.good() == true)
    {
        while(!plik.eof())
        {
            getline(plik, linia);
            cout << linia << endl;
        }
        plik.close();
    }
    getch();
}


int main()
{
    Manager m;
    m.entry();
    while(true)
    {
        m.run();
    }
    return 0;
}
