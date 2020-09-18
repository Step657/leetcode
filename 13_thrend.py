"""
    处理器和核的数量总是有限的，如果线程的数量多于核的数量，就必然需要调度。
    不同的线程可能需要使用到相同的一组寄存器来保存中间计算结果或当前状态。因此在调度线程的时候必须做好上下文保存和恢复工作，
    以保证该线程下次被调度进处理器后能够继续上次的工作。
    threading模块是Python支持多线程的重要模块，该模块是在底层模块_thread的基础上开发的更高层次的线程编程接口。
    常用方法：


"""
