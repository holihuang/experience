<template>
    <div class="wrapper">
        <div class="left">
            <div class="head">
                <img class="img" src="../assets/head.jpg" />
            </div>
            <div class="line">
                <div class="icon">
                    <UserFilled style="width: 1.5em; height: 1.5em;" />
                </div>
                <span>{{state.name}}</span>
            </div>
            <div class="line">
                <div class="icon">
                    <Location style="width: 1.5em; height: 1.5em;" />
                </div>
                <span>{{ state.address }}</span>
            </div>
            <div class="line">
                <div class="icon">
                    <Calendar style="width: 1.5em; height: 1.5em;" />
                </div>
                <span>{{state.year}}年工作经验</span>
            </div>
            <div class="line">
                <div class="icon">
                    <Cellphone style="width: 1.5em; height: 1.5em;" />
                </div>
                <span>{{state.phone}}</span>
            </div>
            <div class="line">
                <div class="icon">
                    <Message style="width: 1.5em; height: 1.5em;" />
                </div>
                <span>{{state.email}}</span>
            </div>
        </div>
        <div class="right">
            <div class="line">
                <div class="title">求职意向</div>
                <div class="job content">{{state.job}}</div>
            </div>
            <div class="line">
                <div class="title">教育背景</div>
                <div class="content">
                    <div v-for="item in state.eduList" :key="item">
                        <div class="education">
                            <div>{{state[item].start}}-{{state[item].end}}</div>
                            <div>{{state[item].subject}}</div>
                            <div>{{state[item].name}}({{state[item].degree}})</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="line">
                <div class="title">专业技能</div>
                <div class="content">
                    <div v-for="(item, index) in state.skills" :key="item">
                        <div>{{index + 1}}. {{item}}</div>
                    </div>
                </div>
            </div>
            <div class="line">
                <div class="title">工作经历</div>
                <div class="content">
                    <div v-for="(item, index) in state.projects" :key="index">
                        <div class="project">
                            <div class="period">
                                {{index+1}}. {{item.start}}-{{item.end}}<div v-if="item.name">({{item.name}})</div>
                            </div>
                            <div class="placeholder"></div>
                            <div>{{item.company}}</div>
                        </div>
                        <div>技术栈：{{item.items.tech}}</div>
                        <div v-for="(itm, index) in item.items.info" :key="itm">
                            <div>{{index+1}}) {{itm}}</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="line">
                <div class="title">自我评价</div>
                <div class="content assess">
                    {{state.assess}}
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
    import {
        reactive,
        onMounted,
    } from 'vue'
    const state = reactive({
        name: '黄豪磊',
        address: '郑州',
        phone: '17710961107',
        year: 5,
        email: '1121844663@qq.com',
        job: '产品经理',
        eduList: ['postgraduate', 'college'],
        postgraduate: {
            name: '北京邮电大学',
            start: '2014.9',
            end: '2017.3',
            degree: '硕士',
            subject: '电子与通信工程',
        },
        college: {
            name: '四川工商学院',
            start: '2009.9',
            end: '2013.6',
            degree: '学士',
            subject: '电子信息工程',
        },
        skills: [
            '熟练使用Axure、Visio、Xmind、Vue、React技术',
            '熟练使用Vue-cli、Webpack等构建工具',
            '熟练使用Linux、Node、Python、Mysql等服务端技术',
            '熟练使用Git、Svn等版本控制工具',
            '有CI、CD等DevOps经验',
            '在移动端、B端系统有丰富的项目经验',
        ],
        projects: [{
            name: '',
            company: '广诚盈信',
            start: '2023.8',
            end: '2024.11',
            items: {
                tech: 'python+tushare+backtrader',
                info: [
                    `基于tushare筛选股票历史交易记录的数据`,
                    `根据交易策略依据backtrader比对历史数据，判断交易策略在历史数据的成功率，然后判断历史成功率是否高于
                    阈值，高于阈值采纳策略，低于阈值重新更新策略
                    `,
                ],
            }
        },{
            name: '学生端',
            company: '领格卓越',
            start: '2022.1',
            end: '2022.4',
            items: {
                tech: 'vue-cli+vue+vuex',
                info: [
                    `学生端约课平台，主要包含约课，支付等模块，负责约课模块的开发`
                ]
            },
        }, {
            name: '彼芯',
            company: '好未来',
            start: '2021.2',
            end: '2021.11',
            items: {
                tech: 'vue-cli + vue + vuex + typescript',
                info: [
                    `彼芯是一款答题的app，采用hybrid（electron + h5）的开发模式，h5内容主要包含答题和
                    错题本两大模块，其中错题本包含首页，单元列表页，查看页面，我的页面，
                    `,
                    `
                    页面开发大量采用了图片（pwa离线缓存），动画（lottie-web动画库），采用pwa技术提高了
                    页面的访问速度，保障了用户体验，
                    `,
                    `
                    页面开发采用vue框架，vue框架双向绑定，让数据操作更容易，组件式开发提高了开发的复用性，
                    virtualDom提高了页面性能。
                    `
                ],
            },
        }, {
            name: '灵犀',
            company: '高途',
            start: '2020.5-2020.12',
            items: {
                tech: 'umi+react+redux+antd',
                info: [
                    `集团IM协同办公平台，包含前台、后台两大模块，其中前台包含消息，工作台等模块`,
                    `消息列表采用虚拟列表技术，提高页面性能`,
                ],
            },
        }, {
            name: '学员故事',
            company: '尚德',
            start: '2017.4',
            end: '2020.5',
            items: {
                tech: 'webpack+react+redux+saga+antd',
                info: [
                    `社区优质案例运营平台，包含前台和后台两大组成部分，前台采用hybrid（h5+native）的开发模式，
                    后台是B端管理系统,
                    `,
                    `
                    后台主要采用异构开发框架backbone+react，基于mvc模型，backbone model做model
                    层，react做view层，用react代替hogan模板,
                    `,
                    `
                    前台采用react全家桶，即react+redux，react单向
                    数据流，数据结构清晰，组件式开发提高复用性，virtualDom提高页面性能，其中首页采用虚拟列表技术
                    和图片懒加载提高页面性能和减少服务器并行压力。
                    `
                ],
            },
        }],
        assess: '逻辑思考能⼒强，能独⽴思考解决问题，有良好的表达沟通能⼒，责任心强，踏实稳重，有强烈的团队意识。',
    })

    function getYear() {
        const year = new Date().getFullYear();
        const month = new Date().getMonth();
        const targeYear = 2017;
        const targteMonth = 4;
        let deltYear = year - targeYear;
        let deltMonth = month - targteMonth;
        if (deltMonth < 0) {
            deltYear--;
        }
        state.year = deltYear;
    }

    onMounted(() => {
        console.log('onmounted...');
        getYear();
    })
</script>
<style lang="less" scoped>
    .wrapper {
        display: flex;
        flex: 1;

        .left {
            width: 250px;
            background: #4169E1;
            color: #fff;

            .head {
                width: 100%;
                display: flex;
                justify-content: center;
                margin: 30px 0;

                .img {
                    width: 56px;
                    height: 82px;
                    border: 2px solid white;
                }
            }

            .line {
                display: flex;

                .icon {
                    margin: 0 12px;
                }
            }
        }

        .right {
            display: flex;
            flex: 1;
            flex-direction: column;
            padding: 15px 30px 15px 20px;

            .line {
                display: flex;
                flex: 1;
                flex-direction: column;

                .title {
                    border-bottom: 2px solid #4169E1;
                }

                .job {
                    display: flex;
                    justify-content: flex-start;
                    align-items: center;
                }

                .content {
                    margin: 15px 0;
                }

                .education {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }

                .project {
                    display: flex;
                    justify-content: flex-start;
                    align-items: center;
                    .period {
                        display: flex;
                    }
                }
                .placeholder {
                    width: 10px;
                }
            }
        }
    }
</style>