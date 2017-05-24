/**
 * Created by firzen on 17-5-24.
 */
var Chess=
    {
        createNew: function (color)
        {
            chess={};
            chess.color=color;
            chess.num=0;              //number of small square contains.
            //the first square set as (0,0);charax and charay mark the shift of other squares.
            chess.charax=new Array(4);
            chess.charay=new Array(4);
            for(let i=0;i<4;i++)
            {
                chess.charax[i]=chess.charay[i]=0;
            }
            chess.rotate=0;           //times of being rotated for 90 degree (0,1,2,3).
            chess.reverse=0;          //whether be reversed (0,1).
            chess.used=0;             //whether be used (0,1).
            chess.draw=draw;          //draw this chess.the upper left of the first square is at (startx,starty).
            function draw(startx,starty)
            {
                let context=drawing.getContext("2d");
                // the chessboard
                context.fillStyle="blue";
                context.strokeStyle="yellow";
                for(let i=0;i<this.num;i++)
                {
                    context.fillRect(startx+this.charax[i]*40, starty-this.charay[i]*40, 40, 40);
                    context.strokeRect(startx+this.charax[i]*40, starty-this.charay[i]*40, 40, 40)
                }
                return "plotted";
            }
            return chess;
        }
    };

function create_chesses(color,player) {
    player.chess=new Array(21);
    for(let i=0;i<21;i++)
        player.chess[i]=Chess.createNew(color);
    let j=0;
    //chess 0
    // .
    player.chess[j].num=1;
    player.chess[j].draw(20,20);
    j++;
    //chess 1
    // ..
    player.chess[j].num=2;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].draw(100,20);
    j++;
    //chess 2
    // ...
    player.chess[j].num=3;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=2;
    player.chess[j].charay[2]=0;
    player.chess[j].draw(220,20);
    j++;
    //chess 3
    //  .
    // ..
    player.chess[j].num=3;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=1;
    player.chess[j].charay[2]=1;
    player.chess[j].draw(380,60);
    j++;
    //chess 4
    // ....
    player.chess[j].num=4;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=2;
    player.chess[j].charay[2]=0;
    player.chess[j].charax[3]=3;
    player.chess[j].charay[3]=0;
    player.chess[j].draw(20,100);
    j++;
    //chess 5
    //  .
    //  .
    // ..
    player.chess[j].num=4;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=1;
    player.chess[j].charay[2]=1;
    player.chess[j].charax[3]=1;
    player.chess[j].charay[3]=2;
    player.chess[j].draw(220,180);
    j++;
    //chess 6
    //  .
    // ...
    player.chess[j].num=4;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=1;
    player.chess[j].charay[2]=1;
    player.chess[j].charax[3]=2;
    player.chess[j].charay[3]=0;
    player.chess[j].draw(340,180);
    j++;
    //chess 7
    // ..
    // ..
    player.chess[j].num=4;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=1;
    player.chess[j].charay[2]=1;
    player.chess[j].charax[3]=0;
    player.chess[j].charay[3]=1;
    player.chess[j].draw(500,60);
    j++;
    //chess 8
    //  ..
    // ..
    player.chess[j].num=4;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=1;
    player.chess[j].charay[2]=1;
    player.chess[j].charax[3]=2;
    player.chess[j].charay[3]=1;
    player.chess[j].draw(20,220);
    j++;
    //chess 9
    // .....
    player.chess[j].num=5;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=2;
    player.chess[j].charay[2]=0;
    player.chess[j].charax[3]=3;
    player.chess[j].charay[3]=0;
    player.chess[j].charax[4]=4;
    player.chess[j].charay[4]=0;
    player.chess[j].draw(140,260);
    j++;
    //chess 10
    //  .
    //  .
    //  .
    // ..
    player.chess[j].num=5;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=1;
    player.chess[j].charay[2]=1;
    player.chess[j].charax[3]=1;
    player.chess[j].charay[3]=2;
    player.chess[j].charax[4]=1;
    player.chess[j].charay[4]=3;
    player.chess[j].draw(500,260);
    j++;
    //chess 11
    //  .
    //  .
    // ..
    // .
    player.chess[j].num=5;
    player.chess[j].charax[1]=0;
    player.chess[j].charay[1]=1;
    player.chess[j].charax[2]=1;
    player.chess[j].charay[2]=1;
    player.chess[j].charax[3]=1;
    player.chess[j].charay[3]=2;
    player.chess[j].charax[4]=1;
    player.chess[j].charay[4]=3;
    player.chess[j].draw(20,420);
    j++;
    //chess 12
    //  .
    // ..
    // ..
    player.chess[j].num=5;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=1;
    player.chess[j].charay[2]=1;
    player.chess[j].charax[3]=1;
    player.chess[j].charay[3]=2;
    player.chess[j].charax[4]=0;
    player.chess[j].charay[4]=1;
    player.chess[j].draw(140,420);
    j++;
    //chess 13
    // ..
    //  .
    // ..
    player.chess[j].num=5;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=1;
    player.chess[j].charay[2]=1;
    player.chess[j].charax[3]=1;
    player.chess[j].charay[3]=2;
    player.chess[j].charax[4]=0;
    player.chess[j].charay[4]=2;
    player.chess[j].draw(260,420);
    j++;
    //chess 14
    //  .
    // ....
    player.chess[j].num=5;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=1;
    player.chess[j].charay[2]=1;
    player.chess[j].charax[3]=2;
    player.chess[j].charay[3]=0;
    player.chess[j].charax[4]=3;
    player.chess[j].charay[4]=0;
    player.chess[j].draw(380,340);
    j++;
    //chess 15
    //  .
    //  .
    // ...
    player.chess[j].num=5;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=1;
    player.chess[j].charay[2]=1;
    player.chess[j].charax[3]=1;
    player.chess[j].charay[3]=2;
    player.chess[j].charax[4]=2;
    player.chess[j].charay[4]=0;
    player.chess[j].draw(20,580);
    j++;
    //chess 16
    //   .
    //   .
    // ...
    player.chess[j].num=5;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=2;
    player.chess[j].charay[2]=0;
    player.chess[j].charax[3]=2;
    player.chess[j].charay[3]=1;
    player.chess[j].charax[4]=2;
    player.chess[j].charay[4]=2;
    player.chess[j].draw(180,580);
    j++;
    //chess 17
    //   .
    //  ..
    // ..
    player.chess[j].num=5;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=1;
    player.chess[j].charay[2]=1;
    player.chess[j].charax[3]=2;
    player.chess[j].charay[3]=1;
    player.chess[j].charax[4]=2;
    player.chess[j].charay[4]=2;
    player.chess[j].draw(340,580);
    j++;
    //chess 18
    //  ..
    //  .
    // ..
    player.chess[j].num=5;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=1;
    player.chess[j].charay[2]=1;
    player.chess[j].charax[3]=1;
    player.chess[j].charay[3]=2;
    player.chess[j].charax[4]=2;
    player.chess[j].charay[4]=2;
    player.chess[j].draw(20,740);
    j++;
    //chess 19
    //  .
    //  ..
    // ..
    player.chess[j].num=5;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=1;
    player.chess[j].charay[2]=1;
    player.chess[j].charax[3]=1;
    player.chess[j].charay[3]=2;
    player.chess[j].charax[4]=2;
    player.chess[j].charay[4]=1;
    player.chess[j].draw(180,740);
    j++;
    //chess 20
    //  .
    // ...
    /// .  this line is y=-1
    player.chess[j].num=5;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=1;
    player.chess[j].charay[2]=1;
    player.chess[j].charax[3]=1;
    player.chess[j].charay[3]=-1;
    player.chess[j].charax[4]=2;
    player.chess[j].charay[4]=0;
    player.chess[j].draw(340,700);
    j++;

    return "created";
}
