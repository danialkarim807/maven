job("first-maven-project-by-DSL"){
    description("first maven job gernated by the SSL on ${new Date()}")
    scm {
        git("https://github.com/danialkarim807/maven.git", main)

    }
    triggers {
        scm("* * * * *")
    }
    step {
        maven("clean package", "pom.xml")

    }
    publishers {
        archiveArtifacts "**/*.war"
    }
}