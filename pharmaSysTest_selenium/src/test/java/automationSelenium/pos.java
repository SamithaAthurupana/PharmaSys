package automationSelenium;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class pos {
    public static void main(String[] args) {

        WebDriverManager.edgedriver().setup();
        WebDriver driver = new EdgeDriver();

        // Logging Application
        driver.manage().window().maximize();
        driver.get("http://127.0.0.1:5500/frontend/login.html");
        WebElement usernameTextBox = driver.findElement(By.id("username"));
        usernameTextBox.sendKeys("admin");
        WebElement passwordTextBox = driver.findElement(By.id("password"));
        passwordTextBox.sendKeys("admin123");
        WebElement loginButton = driver.findElement(By.id("loginBtn"));
        loginButton.click();
        // Wait until dashboard loads
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        wait.until(ExpectedConditions.urlContains("dashboard"));

        // Open POS page
        driver.get("http://127.0.0.1:5500/frontend/pos.html");
        // Redirect
        WebElement actionButton = driver.findElement(By.className("bi-plus-lg"));
        actionButton.click();
        // Redirect
        WebElement printOption = driver.findElement(By.id("printBtn"));
        printOption.click();
        WebElement payButton = driver.findElement(By.id("payBtn"));
        payButton.click();
    }
}
