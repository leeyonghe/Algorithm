- 코틀린으로 구현하였습니다.
- 문제의 이상한점 <br>
   * 아래 입력값과 출력값에서 입력값중 2사람이 동일한 선호도를 1차 2차에 모두 동일하게 선택되었음에도 <br>
    결과는 Jhon Doe로 나온다고 한다... 계속 체크를 해봐야겠지만 동률인 상황에서 나머지 탈락자의 투표를 나눠준다고 한들 달라질수있는지...? <br> <br>
<table>
   <tr>
         <td>
            입력
         </td>
         <td>
            출력
         </td>
   </tr>
   <tr>
         <td>
            <pre>
1<br><br>
3<br>
Jhon Doe<br>
Jane Smith<br>
Sirhan Sirhan<br>
1 2 3<br>
2 1 3<br>
2 3 1<br>
1 2 3<br>
3 1 2<br>
            </pre>
         </td>
         <td>
           <pre>
Check in
           </pre>
         </td>
   </tr>      
</table>
 