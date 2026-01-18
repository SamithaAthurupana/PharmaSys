package automationSelenium;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class Inventory {
    public static void main(String[] args) {
        WebDriverManager.edgedriver().setup();
        WebDriver driver = new EdgeDriver();

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

        driver.manage().window().maximize();
        driver.get("http://127.0.0.1:5500/frontend/inventory.html");

        WebElement updateInventoryBTN =
                wait.until(ExpectedConditions.elementToBeClickable(By.className("bi-pencil-fill")));
        updateInventoryBTN.click();

        WebElement closeInventoryBTN =
                wait.until(ExpectedConditions.elementToBeClickable(By.id("btn-close")));
        closeInventoryBTN.click();



    }
}
