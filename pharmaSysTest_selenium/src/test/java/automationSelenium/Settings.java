package automationSelenium;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class Settings {
    public static void main(String[] args) {
        WebDriverManager.edgedriver().setup();
        WebDriver driver = new EdgeDriver();
        // open the login page
        driver.manage().window().maximize();
        driver.get("http://127.0.0.1:5500/frontend/login.html");
        // fill the login user form
        WebElement usernameTextBox = driver.findElement(By.id("username"));
        usernameTextBox.sendKeys("admin");
        WebElement passwordTextBox = driver.findElement(By.id("password"));
        passwordTextBox.sendKeys("admin123");
        WebElement loginButton = driver.findElement(By.id("loginBtn"));
        loginButton.click();

        // Wait until dashboard loads
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        wait.until(ExpectedConditions.urlContains("dashboard"));
        // Open settings page
        driver.manage().window().maximize();
        driver.get("http://127.0.0.1:5500/frontend/settings.html");

        // Redirect settings fill form options
        WebElement fm_pg_2Btn = wait.until(ExpectedConditions.elementToBeClickable(By.id("fm-pg-2")));
        fm_pg_2Btn.click();
        WebElement fm_pg_3Btn = wait.until(ExpectedConditions.elementToBeClickable(By.id("fm-pg-3")));
        fm_pg_3Btn.click();
        WebElement fm_pg_1Btn = wait.until(ExpectedConditions.elementToBeClickable(By.id("fm-pg-1")));
        fm_pg_1Btn.click();
    }
}
