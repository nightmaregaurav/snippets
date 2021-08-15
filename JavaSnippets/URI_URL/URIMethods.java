/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.net.URI;
import java.net.URISyntaxException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class URIMethods {
    public static void main(String[] args) {
        try {
            String URIBase = "https://www.google.com.np/";
            String URIRelative = "imghp?hl=ne&ogbl";
            
            URI base = new URI(URIBase);
            URI relative = new URI(URIRelative);
            
            URI resolved = base.resolve(relative);
            
            System.out.println("base.toString()  -->  " + base.toString());
            System.out.println("relative.toString()  -->  " + relative.toString());
            System.out.println("resolved.toString()  -->  " + resolved.toString());
            
            System.out.println("base.normalize().toString()  -->  " + base.normalize().toString());
            System.out.println("relative.normalize().toString()  -->  " + relative.normalize().toString());
            System.out.println("resolved.normalize().toString()  -->  " + resolved.normalize().toString());
            
            System.out.println("base.getScheme()  -->  " + base.getScheme());
            System.out.println("relative.getScheme()  -->  " + relative.getScheme());
            System.out.println("resolved.getScheme()  -->  " + resolved.getScheme());
            
            System.out.println("base.getRawSchemeSpecificPart()  -->  " + base.getRawSchemeSpecificPart());
            System.out.println("relative.getRawSchemeSpecificPart()  -->  " + base.getRawSchemeSpecificPart());
            System.out.println("resolved.getRawSchemeSpecificPart()  -->  " + base.getRawSchemeSpecificPart());
            
            System.out.println("base.getSchemeSpecificPart()  -->  " + base.getSchemeSpecificPart());
            System.out.println("relative.getSchemeSpecificPart()  -->  " + relative.getSchemeSpecificPart());
            System.out.println("resolved.getSchemeSpecificPart()  -->  " + resolved.getSchemeSpecificPart());
            
            System.out.println("base.getAuthority()  -->  " + base.getAuthority());
            System.out.println("relative.getAuthority()  -->  " + relative.getAuthority());
            System.out.println("resolved.getAuthority()  -->  " + resolved.getAuthority());
            
            System.out.println("base.getRawAuthority()  -->  " + base.getRawAuthority());
            System.out.println("relative.getRawAuthority()  -->  " + relative.getRawAuthority());
            System.out.println("resolved.getRawAuthority()  -->  " + resolved.getRawAuthority());
            
            System.out.println("base.getUserInfo()  -->  " + base.getUserInfo());
            System.out.println("relative.getUserInfo()  -->  " + relative.getUserInfo());
            System.out.println("resolved.getUserInfo()  -->  " + resolved.getUserInfo());
            
            System.out.println("base.getRawUserInfo()  -->  " + base.getRawUserInfo());
            System.out.println("relative.getRawUserInfo()  -->  " + relative.getRawUserInfo());
            System.out.println("resolved.getRawUserInfo()  -->  " + resolved.getRawUserInfo());
            
            System.out.println("base.getHost()  -->  " + base.getHost());
            System.out.println("relative.getHost()  -->  " + relative.getHost());
            System.out.println("resolved.getHost()  -->  " + resolved.getHost());
            
            System.out.println("base.getPort()  -->  " + base.getPort());
            System.out.println("relative.getPort()  -->  " + relative.getPort());
            System.out.println("resolved.getPort()  -->  " + resolved.getPort());
            
            System.out.println("base.getFragment()  -->  " + base.getFragment());
            System.out.println("relative.getFragment()  -->  " + relative.getFragment());
            System.out.println("resolved.getFragment()  -->  " + resolved.getFragment());
            
            System.out.println("base.getPath()  -->  " + base.getPath());
            System.out.println("relative.getPath()  -->  " + relative.getPath());
            System.out.println("resolved.getPath()  -->  " + resolved.getPath());
            
            System.out.println("base.getQuery()  -->  " + base.getQuery());
            System.out.println("relative.getQuery()  -->  " + relative.getQuery());
            System.out.println("resolved.getQuery()  -->  " + resolved.getQuery());
            
            System.out.println("base.getRawQuery()  -->  " + base.getRawQuery());
            System.out.println("relative.getRawQuery()  -->  " + relative.getRawQuery());
            System.out.println("resolved.getRawQuery()  -->  " + resolved.getRawQuery());
            
        } catch (URISyntaxException ex) {
            Logger.getLogger(URIMethods.class.getName()).log(Level.SEVERE, null, ex);
        }
       
    }
}
