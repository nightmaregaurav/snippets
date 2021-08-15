/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

/**
 *
 * @author nightmare
 */
public class Server {
    public static void main(String[] args) {
        try{
        // Create and bind ServerSocket
        ServerSocket serverSocket = new ServerSocket(8800);
        // Accept request from client
        Socket connectionSocket = serverSocket.accept();
        // Stream to get message from client
        DataInputStream in = new DataInputStream(connectionSocket.getInputStream());
        // Print msg
        System.out.println(connectionSocket.getRemoteSocketAddress() + " --> " + in.readUTF());
        // Stream to send message to server
        DataOutputStream out = new DataOutputStream(connectionSocket.getOutputStream());
        // Send message
        out.writeUTF("Server said hello!");
        // Close Connection
        connectionSocket.close();
        } catch (IOException e){
            e.printStackTrace();
            System.exit(0);
        }  
    }
}
