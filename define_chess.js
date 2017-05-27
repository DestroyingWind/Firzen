/**
 * Created by firzen on 17-5-24.
 */
let chesses=document.getElementById("chesses");
let Chess=
    {
        createNew: function (color)
        {
            chess={};
            chess.color=color;
            chess.num=0;              //number of small square contains.
            //the first square set as (0,0);charax and charay mark the shift of other squares.
            chess.posix=0;
            chess.posiy=0;
            chess.last_pox=0;
            chess.last_poy=0;
            chess.plotted_flag=0;
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
            function draw()
            {
                let context=chesses.getContext("2d");
                // the chess layer
                context.fillStyle=this.color;
                context.strokeStyle="green";
                if(this.plotted_flag===1)
                {
                    for (let i = 0; i < this.num; i++)
                    {
                        context.clearRect(this.last_pox + this.charax[i] * 40-5, this.last_poy - this.charay[i]* 40-5, 50, 50);
                    }
                }
                else if(this.plotted_flag>1)
                {
                    for (let i = 0; i < this.num; i++)
                    {
                        context.clearRect(this.last_pox + this.charax[i] * 40, this.last_poy - this.charay[i] * 40, 40, 40);
                    }
                }
                for(let i=0;i<this.num;i++)
                {
                    context.fillRect(this.posix+this.charax[i]*40, this.posiy-this.charay[i]*40, 40, 40);
                    context.strokeRect(this.posix+this.charax[i]*40, this.posiy-this.charay[i]*40, 40, 40);
                }
                this.plotted_flag++;
                this.last_pox=this.posix;
                this.last_poy=this.posiy;
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
    player.chess[j].posix=20;
    player.chess[j].posiy=20;
    player.chess[j].draw();
    j++;
    //chess 1
    // ..
    player.chess[j].num=2;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].posix=100;
    player.chess[j].posiy=20;
    player.chess[j].draw();
    j++;
    //chess 2
    // ...
    player.chess[j].num=3;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=2;
    player.chess[j].charay[2]=0;
    player.chess[j].posix=220;
    player.chess[j].posiy=20;
    player.chess[j].draw();
    j++;
    //chess 3
    //  .
    // ..
    player.chess[j].num=3;
    player.chess[j].charax[1]=1;
    player.chess[j].charay[1]=0;
    player.chess[j].charax[2]=1;
    player.chess[j].charay[2]=1;
    player.chess[j].posix=380;
    player.chess[j].posiy=60;
    player.chess[j].draw();
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
    player.chess[j].posix=20;
    player.chess[j].posiy=100;
    player.chess[j].draw();
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
    player.chess[j].posix=220;
    player.chess[j].posiy=180;
    player.chess[j].draw();
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
    player.chess[j].posix=340;
    player.chess[j].posiy=180;
    player.chess[j].draw();
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
    player.chess[j].posix=500;
    player.chess[j].posiy=60;
    player.chess[j].draw();
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
    player.chess[j].posix=20;
    player.chess[j].posiy=220;
    player.chess[j].draw();
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
    player.chess[j].posix=140;
    player.chess[j].posiy=260;
    player.chess[j].draw();
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
    player.chess[j].posix=500;
    player.chess[j].posiy=260;
    player.chess[j].draw();
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
    player.chess[j].posix=20;
    player.chess[j].posiy=420;
    player.chess[j].draw();
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
    player.chess[j].posix=140;
    player.chess[j].posiy=420;
    player.chess[j].draw();
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
    player.chess[j].posix=260;
    player.chess[j].posiy=420;
    player.chess[j].draw();
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
    player.chess[j].posix=380;
    player.chess[j].posiy=340;
    player.chess[j].draw();
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
    player.chess[j].posix=20;
    player.chess[j].posiy=580;
    player.chess[j].draw();
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
    player.chess[j].posix=180;
    player.chess[j].posiy=580;
    player.chess[j].draw();
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
    player.chess[j].posix=340;
    player.chess[j].posiy=580;
    player.chess[j].draw();
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
    player.chess[j].posix=20;
    player.chess[j].posiy=740;
    player.chess[j].draw();
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
    player.chess[j].posix=180;
    player.chess[j].posiy=740;
    player.chess[j].draw();
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
    player.chess[j].posix=340;
    player.chess[j].posiy=700;
    player.chess[j].draw();
    j++;

    return "created";
}