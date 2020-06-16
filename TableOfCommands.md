| Command | Effect |
| ------------- | ------------- |
| lazystarter create [ProjectName] [base-template] | Creates base-template which is just a basic landing page (possibly for a portfolio) |
| lazystarter startproject `[name]` base=`[base]` | Creates a directory with the name and base specified by user |
| lazystarter gitignore override = `[type of git-ignore file] | Overrides the default .gitignore file with one specific to your project type, specified by the user |
| lazystarter add-page `[page type]` | The page type (either a default name like landing-page, portfolio-page, contact-page or the name you want for the files “myPage”) would then generate the files inside the working directory |
| lazystarter remove-page `[page type]` | Removes file matching name of `[page type]` from working directory |
| lazystarter new-project `[project type]` | default or custom filesystem name to be created |
| lazystarter remove `[component]` = `[component type]` | Removes component and all associated scripts safely |
| lazystarter landing-page -background-video | Complete website with HTML, CSS, and JS with default background video |
| lazystarter add dark-mode | Convert all compatible components to a dark theme with default dark mode colors |
