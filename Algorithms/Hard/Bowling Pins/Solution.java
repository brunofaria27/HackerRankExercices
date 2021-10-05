import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Result {
    public static int[] pos = new int[300];

    public static String isWinning(int n, String config) {
        int contador = 0;

        List<Integer> arrayPinosJogos = new ArrayList<Integer>();

        for(int i = 0; i < config.length(); i++) {
            if(config.charAt(i) == 'I') {
                contador++;
            } else {
                if(contador != 0) {
                    arrayPinosJogos.add(contador);
                }
                contador = 0;
            }
        }

        if(contador > 0) {
            arrayPinosJogos.add(contador);
        }

        int result = 0;

        for(int i = 0; i < arrayPinosJogos.size(); i++) {
            result ^= calculaGrundy(arrayPinosJogos.get(i));
        }

        if(result != 0) {
            return "WIN";
        } else {
            return "LOSE";
        }

    }

    private static int mex(List<Integer> arr) {
        int mex = 0;

        while(arr.contains(mex)) {
            mex++;
        }
    
        return mex;
    }

    private static int calculaGrundy(int n) {
        if(pos[n] != 0) {
            return pos[n];
        }

        if(n == 0) {
            return 0;
        }

        List<Integer> list = new ArrayList<Integer>();

        for(int i = 1, j = 0; i <= n; i++) {
            if(i <= n / 2) {
                list.add(calculaGrundy(j) ^ calculaGrundy(n - j - 2));
                j++;
            } else {
                list.add(calculaGrundy(j) ^ calculaGrundy(n - j - 1));
                j++;
            }
        }
        
        pos[n] = mex(list);
        return pos[n];
    }

}

public class Solution {

    public static void main(String[] args) throws IOException {
        Scanner entrada = new Scanner(System.in);

        int t = entrada.nextInt();

        for (int i= 0; i< t; i++) {
            int n = entrada.nextInt();

            String config = entrada.next();

            String result = Result.isWinning(n, config);

            System.out.println(result);
        }

        entrada.close();

    }
}