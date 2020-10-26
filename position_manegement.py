#紙Aコップのx座標　紙Aコップのy座標　紙Bコップx座標 紙Bコップy座標
position_base =[[0.0,0.0,2.0,0.0]]
Acup_tukamu = False
Bcup_tukamu = False

"""
使い方
ハンドをつかんだ時は
position_manager(False,False,x,y,True)

ハンドをはなした時は
position_manager(False,False,x,y,False)

Aカップをつかみたい時の手先の位置を知りたいときは
aa = position_manager(True,True,0,0,False)
x = aa[0]
y = aa[1]

BBカップをつかみたい時の手先の位置を知りたいときは
aa = position_manager(True,False,0,0,False)
x = aa[0]
y = aa[1]
"""
def position_manager(master_judge,paper_cup,x,y,tukami):
    global Acup_tukamu
    global Bcup_tukamu
    position_ret=[0.0,0.0]
    if master_judge == True:
        if len(position_base)>0:
           
         #ホンスワン
            if paper_cup == True:
                position_ret[0] = position_base[len(position_base)-1][2]
                position_ret[1] = position_base[len(position_base)-1][3]
                #position_historyの末尾の紙Aコップのx座標y座標
                return position_ret
            else:
                position_ret[0] = position_base[len(position_base)-1][0]
                position_ret[1] = position_base[len(position_base)-1][1]
                #position_historyの末尾の紙Bコップのx座標y座標
                return position_ret
         
        else:
            return position_ret
           
    else:
        #熊谷さん
        #position_base配列の末尾にx,yを追加
        if tukami == True:
            #Aをつかんでいる場合
            if position_base[len(position_base)-1][0] == x and position_base[len(position_base)-1][1] == y:
                position_base.append([x,y,position_base[len(position_base)-1][2],position_base[len(position_base)-1][3]])
                Acup_tukamu = True
            #Bをつかんでいる場合
            elif position_base[len(position_base)-1][2] == x and position_base[len(position_base)-1][3] == y:
                position_base.append([position_base[len(position_base)-1][0],position_base[len(position_base)-1][1],x,y])
                Bcup_tukamu = True
        else:
            #Aをはなした時
            if Acup_tukamu == True:
                position_base.append([x,y,position_base[len(position_base)-1][2],position_base[len(position_base)-1][3]])
                Acup_tukamu = False
            elif Bcup_tukamu == True:
                position_base.append([position_base[len(position_base)-1][0],position_base[len(position_base)-1][1],x,y])
                Bcup_tukamu = False
                
        return position_ret
