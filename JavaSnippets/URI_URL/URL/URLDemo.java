/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package URI_URL.URL;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class URLDemo {
    public static void main(String[] args) {
        try {
            String urlStriing = "https://www.google.com.np/imghp?hl=ne&ogbl";
            
            URL url = new URL(urlStriing);
            
            System.out.println("url.toString()  -->  " + url.toString());
            System.out.println("url.getAuthority()  -->  " + url.getAuthority());
            System.out.println("url.getFile()  -->  " + url.getFile());
            System.out.println("url.getHost()  -->  " + url.getHost());
            System.out.println("url.getPath()  -->  " + url.getPath());
            System.out.println("url.getProtocol()  -->  " + url.getProtocol());
            System.out.println("url.getQuery()  -->  " + url.getQuery());
            System.out.println("url.getRef()  -->  " + url.getRef());
            System.out.println("url.getUserInfo()  -->  " + url.getUserInfo());
            System.out.println("url.getPort()  -->  " + url.getPort());
            
            InputStream is = url.openStream();
            System.out.println(new String(is.readAllBytes()));

            URLConnection c = url.openConnection();
            
            System.out.println(new String(c.getInputStream().readAllBytes()));
            
        } catch (MalformedURLException ex) {
            Logger.getLogger(URLDemo.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(URLDemo.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
