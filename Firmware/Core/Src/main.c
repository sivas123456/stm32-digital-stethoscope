#include "main.h"
#include <string.h>
#include <stdio.h>

ADC_HandleTypeDef hadc1;
UART_HandleTypeDef huart2;

/* Function Prototypes */
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_ADC1_Init(void);
static void MX_USART2_UART_Init(void);

uint32_t analogValue;
char txBuffer[20];

int main(void)
{
  HAL_Init();
  SystemClock_Config();
  MX_GPIO_Init();
  MX_ADC1_Init();
  MX_USART2_UART_Init();

  while (1)
  {
    // Start ADC conversion
    HAL_ADC_Start(&hadc1);

    // Wait for conversion to complete
    if (HAL_ADC_PollForConversion(&hadc1, HAL_MAX_DELAY) == HAL_OK)
    {
      // Read ADC value
      analogValue = HAL_ADC_GetValue(&hadc1);

      // Format value as ASCII string with newline
      sprintf(txBuffer, "%lu\r\n", analogValue);

      // Transmit over USART2
      HAL_UART_Transmit(&huart2, (uint8_t *)txBuffer, strlen(txBuffer), HAL_MAX_DELAY);
    }

    // Sampling delay (~1 kHz)
    HAL_Delay(1);
  }
}
