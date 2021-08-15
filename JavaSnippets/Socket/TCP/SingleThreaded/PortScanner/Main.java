/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.net.Socket;


/**
 *
 * @author nightmare
 */
public class Main {
    public static void main(String[] args) {
        int startPort = 0;
        int endPort = 10000;
        String host = "localhost";
        
        for(int i = startPort; i <= endPort; i++){
            try{
                Socket socket = new Socket(host, i);
                System.out.println("OPEN: " + i);
            } catch (IOException ex) {
                System.err.println("CLOSE: " + i);
            }
        }
    }
}
