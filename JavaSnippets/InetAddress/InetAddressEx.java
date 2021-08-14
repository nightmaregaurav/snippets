package InetAddress;


import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.logging.Level;
import java.util.logging.Logger;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author nightmare
 */
public class InetAddressEx {
    public static void main(String[] args) {
        try {
            InetAddress localhost = InetAddress.getLocalHost();
            InetAddress google = InetAddress.getByName("www.google.com");
            InetAddress facebook = InetAddress.getByName("www.facebook.com");
            System.out.println("localhost Address: "+ localhost.getHostAddress());
            System.out.println("localhost CanonicalHostName: "+ localhost.getCanonicalHostName());
            System.out.println("localhost HostName: "+ localhost.getHostName());
            System.out.println("localhost string: "+ localhost.toString());
            System.out.println("google Address: "+ google.getHostAddress());
            System.out.println("google CanonicalHostName: "+ google.getCanonicalHostName());
            System.out.println("google HostName: "+ google.getHostName());
            System.out.println("google string: "+ google.toString());
            System.out.println("facebook Address: "+ facebook.getHostAddress());
            System.out.println("facebook CanonicalHostName: "+ facebook.getCanonicalHostName());
            System.out.println("facebook HostName: "+ facebook.getHostName());
            System.out.println("facebook string: "+ facebook.toString()); 
        } catch (UnknownHostException ex) {
            Logger.getLogger(InetAddress.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}