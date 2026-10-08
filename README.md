# Layout Logic · 版式逻辑

A portable, content-led layout skill for posters, slides, covers, and editorial pages. Chinese guidance with verified design references; no runtime network or tool dependency.

**Version 0.1.0 · MIT License · 中文为主**

把信息层级、网格、视觉平衡、点线面、留白和图文关系转成可执行的排版方法，并按内容选择小巧思。依据五份《版构》课件和日本及其他地区设计师的代表作品整理，适合设计创建、优化、评审与系列规范。

## 你会得到什么

- 12 条通用原则，区分功能底线、项目约定与表现选择。
- 12 个有使用条件与回退判断的小巧思。
- 11 个作品案例，附来源、观察、可迁移方法与边界。
- 中文/多语排版、网格计算、跨媒介适配与评审方法。
- 8 个行为验收任务与结构校验工具。

这不是日本风格或瑞士网格的固定模板。来源中的密集、极简、几何和手工逻辑各有用途。用户的文案、尺寸、品牌与指定风格优先。**尚未精读《平面设计中的网格系统》正文**；相关状态在来源记录中保留。

## 使用

仓库：[Mtx20050731/layout-logic](https://github.com/Mtx20050731/layout-logic)。可以通过 GitHub 的 **Code → Download ZIP** 下载完整内容。

支持 `SKILL.md` 的宿主可加载 `skills/layout-logic` 整个目录；主文件与参考均用相对路径。`agents/openai.yaml` 是 Codex UI 元数据，其他宿主可按自身规则忽略或转换。不声称所有宿主均已实测。

下载本仓库后，**只把 `skills/layout-logic` 整个目录作为技能安装**，不把仓库根目录作为技能目录。

在 Codex 中，把该目录复制到个人技能目录（通常是 `~/.codex/skills/layout-logic`，设置了 `CODEX_HOME` 时使用其 `skills` 子目录），重新加载技能后调用：

```text
使用 $layout-logic，为一场青年摄影展设计竖版海报。
尺寸 1080×1440；完整文案如下……
先建立阅读路径和图文关系，再选择与主题有关的小巧思。
```

```text
使用 $layout-logic，检查这张海报的主体识别、标题层级和留白。
保持原文案和双色要求，给出可定位的修改并完成调整。
```

```text
使用 $layout-logic，把已有海报重排成手机版和投影版。
保留品牌角色和信息完整性，分别检查成品阅读条件。
```

制作图片、PPT、PDF 或页面需要宿主拥有相应工具。本 Skill 提供排版决策，不捆绑工具、不要求 API Key，也不强制额外联网。用户指定某种风格时，只补充兼容的版式逻辑。

## 决策方式

内容与阅读目标 → 信息角色与字级 → 网格与对齐 → 视觉重量与留白 → 主题相关的小巧思 → 成品条件验证。

这条关系链允许来回调整。规范分为三层：

| 层级 | 作用 | 示例 |
|---|---|---|
| 功能底线 | 保证信息与主体能够被识别 | 必需事实完整、实际尺寸可读、素材使用符合要求 |
| 项目约定 | 让当前项目或系列一致 | 栏数、版心、字级角色、间距、色彩角色 |
| 表现选择 | 根据主题决定记忆点 | 裁切、正负形、重复中的例外、图文穿插 |

评审给出“位置—问题—影响—调整”；创建时完成当前宿主可支持的成品。没有渲染或实际阅读测试时，会说明验证的范围。

## 目录

```text
skills/layout-logic/
  SKILL.md
  agents/openai.yaml
  references/
    principles.md
    techniques.md
    designer-studies.md
    review.md
    provenance.md
examples/evaluation-cases.md
tools/validate.py
LICENSE
```

## 校验和维护

Skill 使用时无依赖。维护者的结构校验使用 Python 3 与 PyYAML：

```sh
python -m pip install PyYAML
python tools/validate.py
```

校验主文件/元数据、相对引用和发布文件边界；这不替代视觉验证。行为验收任务在 [examples/evaluation-cases.md](examples/evaluation-cases.md)，用于宿主或模型变化后的实际回归。不要把未运行的示例任务标成通过。

结构与发布校验见 [VALIDATION.md](VALIDATION.md)，版本变更见 [CHANGELOG.md](CHANGELOG.md)。

来源：[作品研究](skills/layout-logic/references/designer-studies.md)与[课件映射及未完成书籍状态](skills/layout-logic/references/provenance.md)。

## 贡献

改进规则时写清内容条件、预期作用与失败边界；新增案例附可核对的作品出处，区分资料事实、画面观察与自己的推论。保持技能安装目录内自包含，不提交原始课件、书籍、第三方图片、字体或个人路径。修改后运行结构校验；行为验收和视觉验证分别记录。

## License

原创 Skill 文本和校验代码采用 [MIT License](LICENSE)。第三方作品、书籍、课件与字体未包含在包中，也不受本许可证再授权。外部链接是出处，不是免费素材许可证。
