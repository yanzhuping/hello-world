# App 自动化测试

## 一. 测试用例书写注意事项

1.  ```html
    <label
      for="mainsuit3"
      ng-bind="option.text"
      ng-class="{'btn-middle':option.length>4}"
      class="ng-binding"
    >
      牙前突
    </label>
    <input
      type="checkbox"
      ng-model="$ctrl.casedata[$ctrl.optionData.modelname[$parent.$parent.$index]]['one'+option.value]"
      id="mainsuit3"
      class="ng-pristine ng-untouched ng-valid ng-empty"
    />
    ```
    如上述代码的按钮点击时，关键字使用 **app_click**，选择器使用**for**格式，例入**[for=mainsuit3]**；使用 其他的点击使用 **app_click**，选择器直接使用**id** ，例入**ansyl**
2.  元素上滑，使用关键字 **swipeElement_down**

3.  页面上滑，使用关键字**swipeUp**

4.  操作原生元素时，切换 webview 到原生，使用关键字**get_webview**，操作值设置为**native**，操作完原生后，再次切换**webview** ,操作值设置为空

5.  ```html
    <button
      class="teenagers-footer-next disable-user-behavior"
      id="adultnewcase_5"
      on-tap="$ctrl.changeNav($ctrl.verifyMarkObj.index + 1)"
      ng-if="$ctrl.verifyMarkObj.index!==3"
      style="touch-action: auto;"
    >
      下一页
    </button>
    ```

    例入上述代码中含有**on-tap**,关键字使用**app_tap**

6.  代开新的**webview**,使用关键字**switch_to_cur_win**切换窗口,操作结束，再次使用关键字**switch_to_cur_win**，切回当前窗口

## 二、暂存资料校验，遗留问题

1. 儿童加工单：间隙的矫治，邻面去釉，threeShape 无法校验
2. 成人加工单：预留个别间隙，threeShape 无法校验
