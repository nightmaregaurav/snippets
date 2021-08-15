/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.io.InputStream;
import java.net.CookieHandler;
import java.net.CookieManager;
import java.net.CookiePolicy;
import java.net.CookieStore;
import java.net.HttpCookie;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.Date;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class URL_URLConnection {
    public static void main(String[] args) {
        try {
            String urlStriing = "https://www.google.com.np";
            
            URL url = new URL(urlStriing);
            
            CookieManager manager = new CookieManager();
            manager.setCookiePolicy(CookiePolicy.ACCEPT_ALL);
            CookieHandler.setDefault(manager);
            
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
            
            // read web page using url object
            InputStream is = url.openStream();
            System.out.println(new String(is.readAllBytes()));

            
            URLConnection c = url.openConnection();
            
            //  urlConnection configuration
            c.setConnectTimeout(30000);
            c.setReadTimeout(40000);
            
            // read web page using urlConnection object
            System.out.println(new String(c.getInputStream().readAllBytes()));
            
            // Read header field
            System.out.println("Content-Length: " + c.getHeaderField("Content-Length"));
            System.out.println("Content-Type: " + c.getHeaderField("Content-Type"));
            System.out.println("server: " + c.getHeaderField("server"));
            System.out.println("date: " + c.getHeaderField("date"));
            System.out.println("expires: " + c.getHeaderField("expires"));
            System.out.println("age: " + c.getHeaderField("age"));
            System.out.println("last-modified: " + c.getHeaderField("last-modified"));
            System.out.println("set-cookie: " + c.getHeaderField("set-cookie"));
            
            
            HttpURLConnection hc = (HttpURLConnection) c;
            System.out.println("last modified at "+ new Date(hc.getLastModified()));
            System.out.println("ContentEncoding: "+ hc.getContentEncoding());
            System.out.println("ContentType: "+ hc.getContentType());
            System.out.println("RequestMethod: "+ hc.getRequestMethod());
            System.out.println("Content: "+ hc.getContent().toString());
            
            System.out.println("Reading cookies managed by the cookie manager:");
            CookieStore store = manager.getCookieStore();
            List<HttpCookie> cookies = store.getCookies();
            for(HttpCookie cookie:cookies){
                System.out.println(cookie.getName() + ": " + cookie.getValue());
            }
            
        } catch (MalformedURLException ex) {
            Logger.getLogger(URL_URLConnection.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(URL_URLConnection.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
