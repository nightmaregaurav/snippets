/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Socket.TCP.SingleThreaded;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

/**
 *
 * @author nightmare
 */
public class HttpServer {
    public static void main(String[] args) {
        try(ServerSocket serverSocket = new ServerSocket(8800)){ // Create and bind ServerSocket and close automatically when done
            // Keep serving
            while(true){
                // Accept request from client
                Socket connectionSocket = serverSocket.accept();
                // Message to send to browser
                String response = "HTTP/1.1 200 OK\r\n\r\n" 
                        + "Hello World";
                // actual send operation
                connectionSocket.getOutputStream().write(response.getBytes("UTF-8"));
                // Stream reader to get message from browser since browser does not close output stream, directly reading input stream will not work.
                InputStreamReader ir = new InputStreamReader(connectionSocket.getInputStream());
                // Buffered reader to read data in buffer
                BufferedReader br = new BufferedReader(ir);
                // To write output
                String line = br.readLine();
                while (!line.isEmpty()) {
                    System.out.println(line);
                    line = br.readLine();
                }
                connectionSocket.close();
            }
        } catch (IOException e){
            e.printStackTrace();
            System.exit(0);
        }  
    }
}
