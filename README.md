# 制作 RT-Thread Studio 工程

本文档旨在帮助用户快速地建立 RT-Thread Studio 工程，模板支持包提供了 M0, M3, M4, M7 的 make 工程， 以及 M0 的 Scons 工程模板。本文将以 cortex-m0 模板工程为例，讲解如何将用户的开发板支持包添加到 RT-Thread Studio。

## 制作 BSP 支持包

制作 bsp 的方法这里就不在介绍，请参考文档 《开发板支持包设计规范》和 《开发板支持包制作向导》两个文档。

## 添加模板代码到工程

1. 以 STM32CubeMX 为例，生成一个 stm32f030-nucleo 的 MDK工程；

![cubemx](figures/step1.png)

2. 打开生成的工程文件夹所在目录；

3. 复制工程文件夹下文件 和 cortex-m0 模板工程目录下文件到 BSP 支持包工程目录下；

![move](figures/step2.png)

4. 压缩 bsp 包，打开 Studio SDK，导入 bsp 包：

![import](figures/step3.png)

5. 创建工程：

![create](figures/step4.png)

6.工程创建完成后，此时直接编译是无法通过的，需要修改一些配置，下面的步骤将演示如何修改配置保证工程可以编译下载。

![com](figures/step5.png)

## 忽略文件

1. 直接导入的工程，可能会包含有一些不需要的文件，我们需要手动忽略掉这些文件。以本次演示的工程为例：

![ignore](figures/step6.png)

2. 可以看到，在 Drivers 文件目录下包含了许多暂不需要的文件，鼠标右键点击需要忽略掉的文件，选择 Resoure Configurations -> Exclude from Build：

![ignore2](figures/step7.png)

3. 点击 Debug 前面的方框，点击 OK：

![ignore4](figures/step8.png)

4. 此时工程中就看不到该文件，可以看到 RTOS 文件消失了：

![ignore5](figures/step9.png)

5. 根据以上步骤，屏蔽掉工程不需要的文件。

## 添加头文件路径

1. 在项目资源管理器，右键点击工程，选择属性；

2. 添加头文件路径:

![step3](figures/step10.png)

3. 如果头文件路径有误，会看一个黄色的感叹号，此时就要检查一下头文件的路径了：

![include1](figures/step11.png)


## 更改硬件参数

1. 在项目资源管理器，右键点击工程，选择属性；

2. 修改硬件参数；

![step2](figures/step12.png)

## 添加宏定义

1. 在项目资源管理器，右键点击工程，选择属性；

2. 添加宏定义；

![step4](figures/step13.png)

## 添加链接库

1. 在项目资源管理器，右键点击工程，选择属性；

2. 添加链接库，添加一个 C 库为例；

![step5](figures/step14.png)

## 修改链接脚本

模板工程提供了默认的 eclipse 链接脚本文件，修改链接脚本路径：

![link](figures/step15.png)

## 编译工程

以上步骤完成后，编译工程：：

![end](figures/step16.png)

如果编译产生错误，请根据错误提示进行修改。

## 提交 BSP 支持包

1. 清除编译产物，打开工程所在文件：

2. 复制工程内 .settings，.cproject，.project 文件/文件夹 到 bsp 包工程目录下：

   ![copy](figures/step17.png)

3. 重新打包 bsp 包，再次导入 bsp 包，创建工程，进行验证；
4. 编译下载验证完毕后，向 RT-Thread 提交 BSP 支持包。 

