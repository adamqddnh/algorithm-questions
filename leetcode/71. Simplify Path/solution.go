func simplifyPath(path string) string {
    var (
        allPath = strings.Split(path, "/")
        resPath = make([]string, 0)
    )
    for _, onePath := range allPath {
        if onePath == ".." {
            if len(resPath) == 0 {
                continue
            }
            resPath = resPath[:len(resPath)-1]
        } else if len(onePath) == 0 || onePath == "." {
            continue
        } else {
            resPath = append(resPath, onePath)
        }
    }

    return fmt.Sprintf("/%s", strings.Join(resPath, "/"))
}
